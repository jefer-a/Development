import urllib.parse
import urllib.request
import json

url = 'http://192.168.0.103:8080/'

# 三、web学生信息管理程序


def web_3(url):
    try:
        readStudents()
        while True:
            print('\n***学生信息管理系统***')
            print("{:>^16}\n{:>^16}\n{:>^16}".format('1.初始化信息表','2.查看学生记录','3.新增学生记录'))
            print("{:>^16}\n{:>^16}\n".format('4.删除学生记录','5.退出管理程序'))
            option = input('请选择操作选项：')
            if(option == '1'):
                inittialize()
            elif option == '2':
                listStudents()
            elif option == '3':
                insertRow()
            elif option == '4':
                deleteRow()
            elif option == '5':
                break
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
        print('%-16s%-16s%-8s%-4d' % (self.No, self.Name, self.Sex, self.Age))


# 初始化1
# students列表里面存放的时对象student
students = []


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
    else:
        print(st)
    return st

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
    print('%-16s%-16s%-8s%-4s' % ('No', 'Name', 'Sex', 'Age'))
    for s in students:
        s.show()

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

# 二、上传文件学习
def web_2(url):
    # 下载文件时client端需要两次握手
    # 第一次获取文件名称
    # 第二次获取文件
    with open('/python/spider/baiduwenku_out.txt','rb') as text:
        note=text.read()
    fileName='baiduwenku.txt'
    # 1.头声明未处理的纯二进制数据
    headers={'content-type':'application/octet-stream'}
    url=url+'?fileName='+urllib.parse.quote(fileName)
    # 2.封装请求头
    req=urllib.request.Request(url,note,headers)
    try:
        # 3.响应
        resp=urllib.request.urlopen(req)
        message=resp.read().decode()
        print(message)
    except Exception as error:
        print(error)

# 一、GET与POST学习
def web_1(url):
    province='贵州'
    city='贵阳'
    # 1.编码为16进制
    province=urllib.parse.quote(province)
    city=urllib.parse.quote(city)
    with open('/python/spider/baiduwenku_out.txt',encoding='utf-8') as text:
        note=text.read()
    # 2.组织GET参数
    param='?province='+province+'&city='+city
    # 3.组织POST参数
    note='note='+urllib.parse.quote(note)
    try:
        # 4.data数据需要编码为二进制发送
        resp=urllib.request.urlopen(url+param,data=note.encode())
        # 5.响应读取及解码
        html=resp.read().decode()
        print(type(html))
        # print()
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    # index对应不同web程序入口
    index="3"
    url=url+'web_'+index
    eval("web_"+index+'(url)')

    

