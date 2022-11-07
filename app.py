from fastapi import FastAPI
from dbtool.mysqldb import tableInit, insertData, deleteData, checkData
from dbtool.others import beautify
from decimal import Decimal
from collections import defaultdict
import uvicorn
import uuid


tableInit()

app = FastAPI()

@app.get("/")
async def root():
    return "Hello, welcome to sp-money!"

@app.get("/query/{code}")
async def query(code:str):
    result = checkData(code)
    return {"code": code, "record": beautify(result)}

@app.get("/open")
async def openAPI():
    res = str(uuid.uuid1())[:8]
    while len(checkData(res)) != 0:
        res = str(uuid.uuid1())[:8]
    return res

@app.get("/delete/{code}/{index}")
async def delete(code, index):
    deleteData(code, index)
    result = checkData(code)
    return {"code": code, "record": beautify(result)}

@app.get("/pay/{code}/{name}/{target}/{amount}/{item}")
async def pay(code, name, target, amount, item):
    insertData(code, name, target, amount, item)
    result = checkData(code)
    return {"code": code, "record":beautify(result)}

@app.get("/cal/{code}")
async def cal(code):
    h = defaultdict(int)
    result = checkData(code)
    total = 0
    for code, _, name, target, _, amt in result:
        if target != 'all':
            target = target.split(",")
            for t in target:
                h[t.strip()] += amt / Decimal(len(target))
        else:
            total += amt
        h[name] -= amt
    for k, val in h.items():
        h[k] += total / Decimal(len(h))
    calres = []
    cur = [[v, k] for k, v in h.items()]
    cur.sort()
    left, right = 0, len(cur)-1
    calres = []
    while left < right:
        if cur[left][0] == 0: left += 1
        elif cur[right][0] == 0: right -= 1
        else:
            val = min(abs(cur[left][0]), abs(cur[right][0]))
            cur[left][0] += val
            cur[right][0] -= val
            calres.append("{A} needs to pay {B} amount: {amt}".format(A=cur[right][1], B=cur[left][1], amt=abs(val)))
    return {"code": code, "result": "; ".join(calres) if calres else "Nobody needs to pay", "record": beautify(result)}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")