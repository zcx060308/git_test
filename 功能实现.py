import os
#1判断文件是否存在
def del_info():
    if os.path.exists(file_name):
        with open(file_name)as file:
            stu_old=file.readlines()
    else:
        stu_old=[]
    is_find=False
    if stu_old:
        print("查找并删除数据")
    else:
        print("无学生信息")


#2-实现学生的删除
def del_info():
    show()
    id=input("请输入学号：")
    if os.path.exists(file_name):
        with open(file_name,'r')as file:
            stu_old=file.readlines()
    else:
        stu_old=[]
    is_find=False
    if stu_old:
        with open(file_name,'w')as wfile:
            d={}
            for list in stu_old:
                d=dict(eval(list))
                if(d["id"]!=id):
                    selfwfile.write(str(d)+"\n")
                else:
                    is_find=True
            if is_find:
                print("id为%s的学生信息已经被删除"%(id))
            else:
                print("id为%s的学生信息没有找到"%(id))
    else:
        print("无学生信息")
    show()
#3.实现循环
def del_info():
    ctrl=True
    while ctrl:
        show()
        id =input("请输入学号：")
        if os.path.exists(file_name):
            with open(file_name,'r')as file:
                stu_old =file.readlines()
        else:
            stu_old =[]
        is_find =False
        if stu_old:
            with open(file_name,'w') as wfile:
                d = {}
                for list in stu_old:
                    d =dict(eval(list))
                    if(d["id"] !=id):
                        wfile.write(str(d)+ "\n")
                    else:
                        is_find =True
                if is_find:
                    print("id为%s的学生信息已经被删除"%(id))
                else:
                    print("id为%s的学生信息没有找到"%(id))
        else:
            print("无学生信息")
            return
        show()
        mark=input("是否继续(y/n):")
        if mark=='N' or mark=='n':
            ctrl=False
        else:
            ctrl=True
#显示数据
def show():
    stu_list=[]
    if os.path.exists(file_name):
        with open(file_name,'r',encoding='utf-8')as file:
            stu_old=file.readlines()
            for list in stu_old:
                stu_list.append(dict(eval(list)))
            if stu_list:
                show_student(stu_list)
def show_student(stu_list):
    if not stu_list:
        print("无数据")
        return
    format_title="{:^6}{:^12}\t{:^8}\t{:^10}"
    print(format_title.format("ID","姓名","python成绩",("C成绩")))
    format_data ="{:^6}{:^12}\t{:^8}\t{:^10}"
    for list in stu_list:
        print(format_data.format(list.get("id"),list.get("name"),str(list.get("python")),str(list.get("c"))))