# -*- coding: utf-8 -*-
import json
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import jsonify
import os
import subprocess
import pymssql

class MSSQL:
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


ms = MSSQL(host="127.0.0.1", user="sa", pwd="H6503lab", db="Ergos")

app = Flask(__name__)
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/getData', methods=['GET', 'POST'])
def getData():
    sqlquery_forearmsupination = ("SELECT TestRepData.TimeStampMs,TestRepData.Reading "
                                  "FROM TestRepData INNER JOIN (TestReps INNER JOIN (Tests INNER JOIN (Evaluations INNER JOIN Clients ON Evaluations.ClientID = Clients.ClientID) ON Tests.EvaluationID = Evaluations.EvaluationID) ON TestReps.TestID = Tests.TestID) ON TestRepData.TestID = Tests.TestID "
                                  "WHERE (((Clients.RecordNumber)='F001') AND ((Tests.TestDevice)='{B56DF04B-3362-470A-B62D-EB2886ABB333}') AND ((Tests.TestHand)=1));")
    result = ms.ExecQuery(sqlquery_forearmsupination)
    return json.dumps(result)

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5001,
        debug=True
    )