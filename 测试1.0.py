import os

# 假设学生信息存储在名为 'students.txt' 的文件中
file_name = 'students.txt'


def menu():
    print("===============功能菜单===============")
    print("1 录入学生信息")
    print("2 查找学生信息")
    print("3 删除学生信息")
    print("4 修改学生信息")
    print("5 排序")
    print("6 统计学生总人数")
    print("7 显示所有学生信息")
    print("0 退出系统")
    print("=====================================")


def search_info():
    if os.path.exists(file_name):
        stu_quarry = []  # 用来保存查询结果
        mode = input("请选择检索模式(默认--学号查询  8-方向选择(未实现)): ")
        number = ""
        if mode == "" or mode.lower() != "8":
            number = input("请输入学号：")  # 假设使用学号作为查询条件

        # 注意：方向选择未实现，因为通常不使用方向键内容作为文件存储的键

        with open(file_name, 'r', encoding='utf-8') as file:
            student_read = file.readlines()

        for student in student_read:
            d = eval(student)  # 假设每行是一份字典的字符串表示
            if number and d.get('学号') == number:  # 假设字典中有'学号'这个键
                stu_quarry.append(d)

        for student in stu_quarry:
            print(student)  # 打印查询结果

        mark = input("是否退出查询？（yes/no）：")
        return mark == "yes"
    else:
        print("文件不存在，请检查！")
        return True  # 继续循环


def main():
    menu()
    while True:
        option = input("(默认--数字查询)：请按选项(0-7, Enter继续查询)：")
        if option.isdigit() and 0 <= int(option) <= 7:
            if option == "0":
                print("退出系统")
                break
                # 这里可以调用其他函数，如 insert_info(), del_info() 等，但您没有提供这些函数的实现
            # 例如：if option == "1": insert_info()
            # 注意：这些函数需要您自己实现
            print(f"您选择了选项 {option}，但相应功能未实现。")
        elif option == "":
            if search_info():
                break  # 如果用户选择退出查询，则退出循环
        else:
            print("输入错误，请重新输入！")

        # 注意：main() 函数是程序的入口点，应该被调用以运行程序


if __name__ == "__main__":
    main()

    questions_df = pd.read_csv("training_data.csv", sep=',', encoding='unicode_escape')