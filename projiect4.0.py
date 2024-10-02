a="[[1,2],[3,4],[5,6],[7,8],[9,0]]"

print(type(a))

b=eval(a)

print(type(b))

print(b)

a="{1:'a',2:'b'}"
print(type(a))
b=eval(a)
print(type(b))
print(b)

import os


def search_students_by_id(file_name):
    stu_query = []  # 用来保存查询结果
    if not os.path.exists(file_name):
        print("文件不存在！")
        return stu_query  # 返回空列表表示未找到学生

    id_number = input("请输入学号:")
    if id_number == "":
        print("学号不能为空！")
        return stu_query  # 返回空列表表示未输入学号

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                d = dict(eval(line))  # 注意：这里使用 eval 存在安全风险
                if d["id_number"] == id_number:
                    stu_query.append(d)
            except (ValueError, KeyError):
                # 如果 eval 失败或字典中没有 'id_number' 键，则忽略该行
                continue

    return stu_query


# 使用示例
file_name = "students.txt"  # 假设这是包含学生信息的文件名
results = search_students_by_id(file_name)
if results:
    for student in results:
        print(student)
else:
    print("未找到对应学号的学生信息。")

file_name = "external.txt"


def process_file():
    file_name = "internal.txt"  # 局部变量隐藏了外部变量
    print(file_name)  # 输出: internal.txt


print(file_name)  # 输出: external.txt
process_file()

import json


def search_students_by_id(stu_list):
    students = []
    with open(stu_list, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # 去除行尾的换行符
            if line:  # 确保行不为空
                try:
                    student = json.loads(line)  # 尝试将行解析为 JSON
                    students.append(student)
                except json.JSONDecodeError:
                    print(f"无法解析的行: {line}")

                    # 接下来可以根据需要搜索学生


# 调用函数
search_students_by_id('students.test')  # 假设文件名是 students.test


# 查询信息一个文件存在的判断
def search_info2():
    stu_quary = [] #用來保存查詢结果
    if os.path.exists(file_name) : #两种査海校式

        id_number = input("请输入学号：")
        with open(file_name, 'r' , encoding='utf-8') as file:
            stu_read = file.readlines()
            print (stu_read)
            #定义
            for stu in stu_read:
                d = dict(eval (stu) )
                if id is not "" and d["id"]==id:
                    stu_quary.append (d)
    else:
        print("文件不存在！")
        return
    print (stu_quary)
import os
def visit_dir(test_dir):
    for root, dirs, files in os.walk(test_dir, topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
if __name__ == '__main__':
    visit_dir("D:\PycharmProjects")




