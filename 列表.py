#1--最简单流程
def insert_info():
    stu_list=[]
    id=input("请输学号ID（如001）：")
    name=input("请输入姓名：")

    python_score=int(input("请输入python成绩；"))
    c_score=int (input("请输入c成绩："))

    stul={"id":id, "name":name,"python":python_score,"c":c_score}
    stu_list. append (stul)
    print (stu_list)

#异常数据处理

