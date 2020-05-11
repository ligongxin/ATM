# __author__:'lgx'
# date:2020/5/11 0011
import easygui as g

g.msgbox('需要输入app路径和app的检查包exce表','安卓打包')
msg1='app_excel:\n1、正念\n2、flome\n3、孕迹\n4、能量闹钟'
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
# g.msgbox(b,'安卓打包')
g.textbox(b,'安卓打包')