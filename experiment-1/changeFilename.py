import os
import datetime
path = input("请输入文件夹路径:\n") #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
for file in files: #遍历文件夹
    if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
        filename=file.split(".")#分割文件名和文件后缀
        if "-" in filename[0]:#判断是否已存在时间后缀
            old=filename[0].split("-")
            length=len(old)
            date=old[length-1]
            for i in range(4):
                date=old[length-2-i]+'-'+date
            try:
                datetime.datetime.strptime(date,'%Y-%m-%d-%H-%M')#判断是否符合标准时间表达式
                print("true\n")
                oldname=old[0]
                for i in range(1,len(old)-5):
                    oldname=oldname+'-'+old[i]
            except ValueError:
                oldname=file
        else:
            oldname=filename[0]
        #添加或更新时间后缀
        if len(filename)>1:
            newname=oldname+'-'+ datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')+'.'+filename[1]
        else:
            newname=oldname+'-'+ datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        #修改文件名
        os.rename(file,newname)
