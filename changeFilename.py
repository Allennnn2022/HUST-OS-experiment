import os
import datetime
path = input("�������ļ���·��:\n") #�ļ���Ŀ¼
files= os.listdir(path) #�õ��ļ����µ������ļ�����
s = []
for file in files: #�����ļ���
    if not os.path.isdir(file): #�ж��Ƿ����ļ��У������ļ��вŴ�
        filename=file.split(".")#�ָ��ļ������ļ���׺
        if "-" in filename[0]:#�ж��Ƿ��Ѵ���ʱ���׺
            old=filename[0].split("-")
            length=len(old)
            date=old[length-1]
            for i in range(4):
                date=old[length-2-i]+'-'+date
            try:
                datetime.datetime.strptime(date,'%Y-%m-%d-%H-%M')#�ж��Ƿ���ϱ�׼ʱ����ʽ
                print("true\n")
                oldname=old[0]
                for i in range(1,len(old)-5):
                    oldname=oldname+'-'+old[i]
            except ValueError:
                oldname=file
        else:
            oldname=filename[0]
        #��ӻ����ʱ���׺
        if len(filename)>1:
            newname=oldname+'-'+ datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')+'.'+filename[1]
        else:
            newname=oldname+'-'+ datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        #�޸��ļ���
        os.rename(file,newname)
