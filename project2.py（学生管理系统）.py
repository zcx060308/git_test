import os
file_name="student.txt"
#菜单
def mnenu():
    print('''
            -------------学生管理系统-------------
          |      ==========功能菜单==========     |
          |     1 录入学生信息                     |
          |     2 查找学生信息                     |
          |     3 删除学生信息                     |
          |     4 修改学生信息                     |
          |     5 排序学生信息                     |                           
          |     6 统计学生信息                     |
          |     7 显示所有学生信息                  |
          |     0 退出学生信息系统                  |
          |    ==============================    |
          |  说明：通过数字或↑↓方向键选择菜单          |
            ------------------------------------
           ''')

#选择进行项目
def main():
    mnenu()
    option=input("请选择: ")
    if option=="1":
        print("您选择了录入学生信息")
        insert_info()
    elif option=="2":
          print("您选择了查找学生信息")
          search()
    elif option=="3":
          print("您选择了删除学生信息")
    elif option=="4":
          print("您选择了修改学生信息")
    elif option=="5":
         print("排序学生信息")
    elif option=="6":
          print("您选择了统计学生信息")
    elif option=="7":
          print("您选择了显示学生信息")
    else:
         print("输入错误，请重新输入。")

#录入学生信息
def insert_info():
    student_list=[]
    ctrl=True
    while ctrl:
          id=input("请输入学号ID(如001):")
          if  len(id) <3 or len(id) >3:#限制学号只能输入三位数字
              print("学号输入错误！！！")
              break
          name=input("请输入姓名:")
          if name.lstrip()=="":
             print("学生姓名不能为空！！！")
             break
          # 异常数据处理
          try:
               python_score = int(input("请输入python成绩："))
               c_score = int(input("请输入c语言成绩："))
          except:
                 print("您输入的成绩有误，请重新输入！！！")
                 continue
          student={"学号ID":id,"姓名":name,"python成绩":python_score,"c成绩":c_score}
          student_list.append(student)
          print(student)#显示录入学生信息
          is_exit=input("是否退出？(yes/no):")#选择是否退出录入学生信息系统
          if is_exit=="yes":
              ctrl=False
          else:
              print("----下一学生信息----")
    save_info(student_list)
    print(student_list)

#保存录入数据到file_name文件中
def save_info(student_list):
    try:
        file_text=open(file_name,'a',encoding='utf-8')
    except:
        file_text=open(file_name,'w',encoding='utf-8')

    for student in student_list:
        file_text.write(str(student)+"\n")
    if file_text:
        file_text.close()

#查找学生信息系统
def search():

    ctrl=True
    while ctrl:
        if os.path.exists(file_name):
            student_query = []
            mode = input("请选择查询模式(1-学号查询  2-姓名查询):")
            id = ""
            name = ""
            if mode == "1":
                id = input("请输入学号ID：")
            elif mode == "2":
                name = input("请输入姓名：")
            else:
                print("无效查询模式！")
                return

            with open(file_name, 'r', encoding='utf-8') as file:
                student_read = file.readlines()

            for student in student_read:
                d = dict(eval(student))
                if id != "" and d["学号ID"] == id or name != "" and d["姓名"] == name:
                    student_query.append(d)
                print(student_query)
            mark = input("是否退出查询？（yes/no）")
            if mark == "yes":
                ctrl = False
            else:
                 print("----下一学生信息---")
        else:
            print("文件不存在！！！")

    #函数入口
if __name__ == '__main__':
    main()