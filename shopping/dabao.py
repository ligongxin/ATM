# __author__:'lgx'
# date:2020/5/11 0011
import easygui as g

g.msgbox('��Ҫ����app·����app�ļ���exce��','��׿���')
msg1='app_excel:\n1������\n2��flome\n3���м�\n4����������'
list1=['check_app_path','check_excel_code']
text=g.multenterbox(msg1,title='check_app',fields=list1)
li=[]
def foo():
    for i in range(10):
        li.append(i)
    return li
a=str(foo())
a=a[1:-1]
b=a.replace(',','\n')

print(b)
# g.msgbox(b,'��׿���')
g.textbox(b,'��׿���')