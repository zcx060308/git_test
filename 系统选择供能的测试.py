def main():
    menu()
    option = input("(默认--数字查询/8--⬆⬇方向键选择菜单)：请按(Enter)")
    ctrl = True
    while ctrl:
        if os.path.exists(file_name):  # 两种选择方式
            stu_quarry = []  # 用來保存查詢结果
            number = ""
            direction = ""
            mode = input("请选择检索模式(默认--学号查询  8-方向查询):")
            if mode == "":
                number = input("请输入数字：")
            elif mode == "8":
                direction1 = input("请输入(⬆):")
            elif mode == "8":
                direction2 = input("请输入(⬇):")
            else:
                print("无效选择！")
                return
            with open(file_name, 'r', encoding='utf-8') as file:
                student_read = file.readlines()
            # 定义
            for student in student_read:
                d = dict(eval(student))
                if number != "" and d["数字"] == number or direction1 != "" and d["⬆"] == direction or direction2 != "" and d["⬇"] == direction::
                    stu_quarry.append(d)
                    print(stu_quarry)
            mark = input("是否退出选择？（yes/no）：")
            if mark == "yes":
                ctrl = False
            else:
                ctrl = True
                print("----您已安全提出选择系统----")
        else:
            print("选择无效，请等待系统刷新...")
    if option == "1":
        print("您选择了录入学生信息")
        insert_info()
    elif option == "2":
        print("您选择了查找学生信息")
        search_info2()
    elif option == "3":
        print("您选择了删除学生信息")
        del_info()
    elif option == "4":
        print("您选择了修改学生信息")
        modify_infor()
    elif option == "5":
        print("您选择排序学生信息")
        sort_info()
    elif option == "6":
        print("您选择了统计学生信息")
        total_info()
    elif option == "7":
        print("您选择了显示所有学生信息")
        show()
    elif option == "0":
        out_info()
    else:
        print("输入错误，请重新输入=！")