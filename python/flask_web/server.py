import flask
import os
import sqlite3
import json
import webscript

app = flask.Flask(__name__)

@app.route('/')
def index():
    with open('/python/flask_web/infommanager.html','r',encoding='utf-8') as html:
        html=html.read()
    print('成功访问根目录')
    return html


@app.route('/manager')
def manager():
    opt = flask.request.values.get('opt')\
        if "opt" in flask.request.values else ''
    if opt == "init":
        webscript.web_3(1)
    elif opt=='insert':
        pass
    else:
        webscript.web_3(2)
    # elif opt == 'insert':
    #     # No = flask.request.values.get('No')\
    #     #     if 'No' in flask.request.values else ''
    #     # Name = flask.request.values.get('Name')\
    #     #     if 'Name' in flask.request.values else ''
    #     # Sex = flask.request.values.get('Sex')\
    #     #     if 'Sex' in flask.request.values else ''
    #     # Age = flask.request.values.get('Age')\
    #     #     if 'Age' in flask.request.values else ''
    #     # res = db.insertRow(No, Name, Sex, Age)
    # elif opt == 'delete':
    #     # No = flask.request.values.get('No')\
        #     if 'NO' in flask.request.values else ''
        # res = db.deleteRow(No)
    # else:
        # res=db.selectRows()
    with open('/python/flask_web/back.html','r',encoding='utf-8') as html:
        html=html.read()
    print('操作成功')
    return html

# web学生信息管理系统web_3
@app.route('/web_3', methods=['GET','POST'])
# 接口
def process():
    opt = flask.request.values.get('opt')\
        if "opt" in flask.request.values else ''
    res = {}
    db = studentDB()
    db.openDB()
    if opt == "init":
        res = db.ininTable()
    elif opt == 'insert':
        No = flask.request.values.get('No')\
            if 'No' in flask.request.values else ''
        Name = flask.request.values.get('Name')\
            if 'Name' in flask.request.values else ''
        Sex = flask.request.values.get('Sex')\
            if 'Sex' in flask.request.values else ''
        Age = flask.request.values.get('Age')\
            if 'Age' in flask.request.values else ''
        res = db.insertRow(No, Name, Sex, Age)
    elif opt == 'delete':
        No = flask.request.values.get('No')\
            if 'NO' in flask.request.values else ''
        res = db.deleteRow(No)
    else:
        res=db.selectRows()
    db.closeDB()
    return json.dumps(res)


# 定义一个类封装数据库连接\关闭\操作功能
class studentDB:
    def openDB(self):
        # 连接数据库
        self.con = sqlite3.connect('students.db')
        # 获取数据库操作游标
        self.cursor = self.con.cursor()

    def closeDB(self):
        self.con.commit()
        self.con.close()

    # 创建学生表
    def ininTable(self):
        res = {}
        try:
            self.cursor.execute(
                "create table students(No varchar(16)primary key,Name varchar(16),Sex varchar(8),Age int)")
            res['msg'] = 'ok'
        except Exception as error:
            res['msg'] = str(error)
        return res

    # 插入
    def insertRow(self, No, Name, Sex, Age):
        res = {}
        try:
            self.cursor.execute(
                "insert into students(No,Name,Sex,Age) values(?,?,?,?)", (No, Name, Sex, Age))
            res['msg'] = 'ok'
        except Exception as error:
            res['msg'] = str(error)
        return res

    # 删除
    def deleteRow(self, No):
        res = {}
        try:
            self.cursor.execute("delete from students where No=?", (No,))
            res['msg'] = 'ok'
        except Exception as error:
            res['msg'] = str(error)
        return res

     # 查找
    def selectRows(self):
        res = {}
        try:
            data = []
            self.cursor.execute("select * from students order by No")
            rows = self.cursor.fetchall()
            for row in rows:
                d = {}
                d['No'] = row[0]
                d['Name'] = row[1]
                d['Sex'] = row[2]
                d['Age'] = row[3]
                data.append(d)
                res['msg'] = 'ok'
                res['data'] = data
        except Exception as error:
            res['msg'] = str(error)
        return res


# 对应client端web_2
@app.route('/web_2', methods=['GET', 'POST'])
def index_2():
    try:
        # 1.获取文件名
        fileName = flask.request.args.get('fileName')\
            if 'fileName' in flask.request.args else ''
        if fileName:
            # 2.判断文件是否存在
            if not os.path.exists(fileName):
                # 3.以get_data()方法获取纯二进制数据
                data = flask.request.get_data()
                with open('/python/flask_web/'+fileName, 'wb') as fo:
                    fo.write(data)
                    msg = '上传成功'
            else:
                msg = '文件已存在'
        else:
            msg = '文件名为空'
        print(msg)
        return msg
    except Exception as error:
        print(error)


# 对应client端的web_1()
@app.route('/web_1', methods=['POST', 'GET'])
def index_1():
    try:
        # args\form可统一为values
        with open('/python/spider/baiduwenku_out.txt', encoding='utf-8') as text:
            note = text.read()
        province = flask.request.args.get('province')\
            if 'province' in flask.request.args else ''
        city = flask.request.values.get('city')\
            if 'city' in flask.request.args else ''
        note = flask.request.form.get('note')\
            if 'note' in flask.request.form else note
        print(province+'\t'+city)
        # print(note){'province':province,'city':city}
        return province+city+note
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
