"""
reference: https://learn.microsoft.com/zh-cn/azure/mysql/single-server/connect-python
"""
import os
from dbutils.pooled_db import PooledDB
import pymysql

MYSQL_CONN_POOL = PooledDB(
    creator=pymysql,
    maxconnections=1000,
    mincached=100,
    blocking=True,
    host=os.getenv("MYSQL_HOST"),
    port=3306,
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PWD"),
    database=os.getenv("MYSQL_DATABASE"),
    ssl_ca="dbtool/CA.pem",
)


def tableInit():
    """
    create money table

    """
    conn = MYSQL_CONN_POOL.connection()
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS MONEY\
        (code varchar(8), idx INT UNSIGNED, payer text not null, target text not null, item text, amount decimal(8, 2))"
    )


def insertData(code, payer, target, amount, item):
    cur = checkData(code)
    index = max([val[1] for val in cur]) if cur else 0
    index += 1
    conn = MYSQL_CONN_POOL.connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO money (code, idx, payer, target, item, amount) VALUES (%s, %s, %s, %s, %s, %s)",
        (code, index, payer, target, item, amount),
    )
    conn.commit()


def checkData(code):
    conn = MYSQL_CONN_POOL.connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MONEY WHERE code=%s", code)
    res = cursor.fetchall()
    return res


def deleteData(code, index):
    conn = MYSQL_CONN_POOL.connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM MONEY WHERE code=%s AND idx=%s", (code, index))
    conn.commit()
