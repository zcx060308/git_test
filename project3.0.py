'''magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)'''



# for 循环  (一定要缩进)
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")



#保存数据到file name文件
def save_info(stu list):
    try:
        file text=open(file_name,'a',encoding='utf-8')
    except:
        file text=open(file_name,'a'encoding='utf-8')
#从1ist中去数据的过程
for stu in stu list:
    file_text.write(str(stu)+"\n")
if file text:
    file_textclose()
#打开文件


#关闭文件




