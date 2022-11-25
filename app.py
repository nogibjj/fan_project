from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from dbtool.mysqldb import tableInit, insertData, deleteData, checkData
from dbtool.others import beautify, calculateRel, deleteFileRegex
import uvicorn
import uuid
import csv


tableInit()

app = FastAPI()


@app.get("/")
async def root():
    return "Hello, welcome to sp-money!"


@app.get("/query/{code}")
async def query(code: str):
    result = checkData(code)
    return {"code": code, "record": beautify(result)}


@app.get("/open/{password}")
async def openAPI(password: str):
    print(password)
    res = str(uuid.uuid1())[:8]
    while len(checkData(res)) != 0:
        res = str(uuid.uuid1())[:8]
    return res


@app.post("/delete/{code}/{index}")
async def delete(code, index):
    deleteData(code, index)
    result = checkData(code)
    return {"code": code, "record": beautify(result)}


@app.get("/pay/{code}/{name}/{target}/{amount}/{item}")
async def pay(code, name, target, amount, item):
    insertData(code, name, target, amount, item)
    result = checkData(code)
    return {"code": code, "record": beautify(result)}


@app.get("/cal/{code}")
async def cal(code):
    result = checkData(code)
    cal_rels = calculateRel(result)
    calres = []
    for payer, target, amt in cal_rels:
        calres.append(
            "{A} needs to pay {B} amount: {amt}".format(A=payer, B=target, amt=amt)
        )

    return {
        "code": code,
        "result": "; ".join(calres) if calres else "Nobody needs to pay",
        "record": beautify(result),
    }


@app.post("/download/{code}")
async def download(code: str):
    data = checkData(code)
    if len(data) == 0:
        return JSONResponse(content="NO DATA", status_code=403)
    deleteFileRegex(code, "static/")
    filepath = "static/" + str(uuid.uuid1()) + "_" + code + ".csv"
    calres = calculateRel(data)
    with open(filepath, "w", encoding="utf-8") as f:
        header = ["item", "payer", "users", "money"]
        writer = csv.writer(f)
        writer.writerow(header)
        for _, _, name, target, item, amt in data:
            writer.writerow([item, name, target, amt])
        writer.writerow("")
        writer.writerow(["PAY RELATIONSHIP"])
        writer.writerow(["Sender", "Receiver", "Money"])
        for sender, receiver, money in calres:
            writer.writerow([sender, receiver, money])

    return FileResponse(filepath, filename="{code}.csv".format(code=code))


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
