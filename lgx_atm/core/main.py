#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/3012:40
#文件     :
#IDE      :PyCharm
from lgx_atm.core import logger
from lgx_atm.core import auth,accounts


#user_data,记住用户是否登录
user_data={
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}


# 主流程，用户登录 auth_login
#定义日志
account_logger=logger.logger('account')  #账户日志

def account_info(acc_data):
    print(acc_data)

def repay(acc_data):
    '''还款'''
    #获取最新的数据
    new_account_data=accounts.load_current_account(acc_data['id'])
    current_balance='''------------- BALANCE INFO ---------------
    Credit:{0}
    Balance:{1}'''.format(new_account_data['credit'],new_account_data['balance'])
    print(current_balance)


def withdraw(acc_data):
    pass

def transfer(acc_data):
    pass

def pay_check(acc_data):
    pass

def logout(acc_data):
    print('Welcome to come again!')
    exit()

def interactive(acc_data):
    '''业务菜单'''
    menu = u'''
    ------- Oldboy Bank ---------
    \033[32;1m1.  账户信息
    2.  还款(功能已实现)
    3.  取款(功能已实现)
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''
    menu_dic={
        '1':account_info,
        '2':repay,
        '3':withdraw,
        '4':transfer,
        '5':pay_check,
        '6':logout
    }
    exit_fiag=False
    while not exit_fiag:
        print(menu)
        user_option=input('>>:').strip()
        if user_option in menu_dic:
            print('accdata:%s'%acc_data)
            #执行对应的业务
            menu_dic[user_option](acc_data)
        else:
            print('"\033[31;1mOption does not exist!\033[0m"')


def run():
    #用户登录
    acc_data=auth.acc_login(user_data,account_logger)
    #展示业务菜单
    interactive(acc_data)


if __name__=='__main__':
    run()