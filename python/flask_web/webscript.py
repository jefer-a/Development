import urllib.parse
import urllib.request
import json
import re

url = 'http://192.168.0.103:8080/web_3'

# 三、web学生信息管理程序


def web_3(option):
    try:
        readStudents()
        if(option == 1):
            inittialize()
        elif option == 2:
            listStudents()
        elif option == 3:
            insertRow()
        elif option == 4:
            deleteRow()
        elif option ==5:
            return
    except Exception as excepts:
        print(excepts)


# 定义类以封装操作功能
class student:
    # 初始化实例对象，初始化数据库表头
    def __init__(self, No, Name, Sex, Age):
        self.No = No
        self.Name = Name
        self.Sex = Sex
        self.Age = Age

    def show(self):
        line=''
        line=('%-16s%-16s%-8s%-4d' % (self.No, self.Name, self.Sex, self.Age))
        print('line')
        return line

# 初始化1
# students列表里面存放的时对象student
students = []

def htmlWrite(resp):
    with open('/python/flask_web/infommanager.html','r',encoding='utf-8') as fo1:
        infommanager=fo1.readlines()
    index=0
    for line in infommanager:
        if '<!--operation-->' in line:
            break
        index+=1
    infommanager.insert(index,resp)
    with open('/python/flask_web/back.html','w',encoding='utf-8') as fo2:
        fo2.writelines(infommanager)


def inittialize():
    st = ''
    try:
        content = urllib.request.urlopen(url+'?opt=init')
        st = content.read()
        st = json.loads(st.decode())
        st = st['msg']
    except Exception as error:
        st = str(error)
    if st == 'ok':
        print('初始化成功')
        resp='初始化成功'
    else:
        print(st)
        resp=st
    htmlWrite(resp)

# 读取数据库更新students列表


def readStudents():
    global students
    try:
        students.clear()
        content = urllib.request.urlopen(url)
        data = b''
        while True:
            buf = content.read(1024)
            if (len(buf) > 0):
                data = data+buf
            else:
                break
        data = data.decode()
        data = json.loads(data)
        if data['msg'] == 'ok':
            data = data['data']
            for d in data:
                # each d is a dictionary
                s = student(d['No'], d['Name'], d['Sex'], d['Age'])
                students.append(s)
    except Exception as error:
        print(error)

# 查看信息表2


def listStudents():
    global students
    table='<div style="margin-left:20px;"><table><tr>'
    resp='<td style="width: 60px;">No</td><td style="width: 60px;">Name</td><td style="width: 60px;">Sex</td><td style="width: 60px;">Age</td></tr>'
    resp=table+resp
    for s in students:
        print(type(s.Age))
        # line=('%-16s%-16s%-8s%-4s' % (s.No, s.Name, s.Sex, s.Age))
        line='<td style="width: 60px;">'+s.No+'</td><td style="width: 60px;">'+s.Name+'</td><td style="width: 60px;">'+s.Sex+'</td><td style="width: 60px;">'+str(s.Age)+'</td></tr>'
        # print('{:-^16s%}{:-^16s%}{:-^8s%}{:-^4d%}'.format(s.No,s.Name,s.Sex,s.Age))
        resp=resp+'\n'+line
    resp=resp+'</table></div>'
    print("查询成功")
    htmlWrite(resp)

# 插入3


def insertStudent(s):
    global students
    index = 0
    while (index < len(students) and s.No > students[index].No):
        index += 1
    if(index < len(students) and s.No == students[index].No):
        print(s.No+"already exists")
        return False
    students.insert(index, s)
    return True

def insertRow():
    No = input('No=')
    Name = input('Name=')
    while True:
        Sex = input('Sex=')
        if Sex == '男' or Sex == '女':
            break
        else:
            print('Sex is not valid')
    while True:
        Age = input('Age=')
        if(Age == ''):
            Age = 0
        else:
            try:
                Age = int(Age)
                break
            except Exception as ex:
                print('Age输入错误:\n',ex)
    if No != '' and Name != '':
        s= student(No, Name, Sex, Age)
        for x in students:
            if (x.No == No):
                print(No+' already exists')
                return
        st = ''
        try:
            st= 'No='+urllib.request.quote(No)+"&Name="+urllib.request.quote(
                Name
            )+'&Sex='+urllib.request.quote(Sex)+'&Age='+str(Age)
            st=st.encode()
            content=urllib.request.urlopen(url+'?opt=insert',st)
            st=content.read()
            st=json.loads(st.decode())
            st=st['msg']
        except Exception as error:
            st=str(error)
        
        if (st=='ok'):
            insertStudent(s)
            print('新增成功')
        else:
            print(st)
    else:
        print('学号、姓名不能为空')

# 删除4
def deleteRow():
    global students
    No=input('No=')
    if (No!=''):
        for i in range(len(students)):
            if(students[i].No==No):
                st=''
                try:
                    st='No='+urllib.request.quote(No)
                    st=st.encode()
                    content=urllib.request.urlopen(url+'?opt=delete',st)
                    st=content.readline()
                    st=json.loads(st.decode())
                    st=st['msg']
                except  Exception as error:
                    st=str(error)
                
                if (st=='ok'):
                    del students[i]
                    print('删除成功')
                else:
                    print(st)
                break


if __name__ == '__main__':
    # index对应不同web程序入口
    index="3"
    eval("web_"+index+'(url)')

    

