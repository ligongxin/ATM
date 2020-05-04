#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/3012:40
#文件     :
#IDE      :PyCharm
from lgx_atm.core import logger
from lgx_atm.core import auth,accounts,transaction


#user_data,记住用户是否登录
user_data={
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}


# 主流程，用户登录 auth_login
#定义日志
account_logger=logger.logger('account')  #账户日志
transaction_logger=logger.logger('transaction') #交易记录

def account_info(acc_data):
    acc_info='''------------- BALANCE INFO ---------------
    卡号:{0}
    余额:{1}
    额度:{2}
    过期时间:{3}
    还款日:{4}
    '''.format(acc_data['id'],acc_data['credit'],acc_data['balance'],acc_data['expire_date'],acc_data['pay_day'])
    print(acc_info)

def repay(acc_data):
    '''还款'''
    #获取最新的数据
    new_account_data=accounts.load_current_account(acc_data['id'])
    current_balance='''------------- BALANCE INFO ---------------
    Credit:{0}元
    Balance:{1}元'''.format(new_account_data['credit'],new_account_data['balance'])
    print(current_balance)
    #进行还款操作
    repay_flag=True
    while repay_flag:
        repay_amount=input('"\033[33;1mInput repay amount:\33[0m').strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            new_balance=transaction.make_transaction(transaction_logger,acc_data,'repay',repay_amount)
            if new_balance:
                print('new_balance:%s'%new_balance)
        else:
            print('repay amount is valid,')
        if repay_amount == 'b':
            repay_flag =False

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
            # print('accdata:%s'%acc_data)
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