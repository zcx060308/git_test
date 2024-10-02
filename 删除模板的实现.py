def modifr_infor():
    show()
    if os.path.erists(file_nane):
        with ooen(file_mane,'r',eocoding='utf-8') as file:
            stu_old=file.readlines()
    else:
        print("文件不存在")
        return
    is_mofidy=True
    if stu_old:
        id=input("请输入要修改学生的学号")
        with open(file_name,'w',eocoding="utf-8") as fi1e_new:
            for stu in stu_old:
                d=dict(eval(stu))
                if d["id"]==id:
                    print("找到了学生,可以修改他的信息!")
                    is _mofidy=False
                    while True:
                        try:
                            d["nane"]=input("请验入姓名:")
                            d["python"]=int(input("请输入python的成绩:")
                            d["c"]=int(input("请输入C语言的成绩,"))
                        except ValueError:
                            print("您的输入有误,请重新输入")
                        else:
                            break

                    file_new.write(str(d)+"\n")
                    print("数据修改成功")
                else:
                    file_new.write(stu)
            if is_mofidy:
                print("没找到该学生")
        else:
            print("没有学生数招")
        mark=input("是否维续修改学生信息(y/n):")
        if mark=='Y' or mark== "y":
            modify_infor()
