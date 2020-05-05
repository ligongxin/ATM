# _*_encoding=utf-8_*_
# 作者     :bozhong
# 创建时间 :2020/4/3012:39
# 文件     :
# IDE      :PyCharm
from lgx_atm.core import accounts
import time

def login_required(func):
    '''验证是否登录'''
    def wrapper(*args,**kwargs):
        if args[0].get('is_authenticated'):
            return func(*args,**kwargs)
        else:
            print('你未登录')
    return wrapper


def acc_auth(account, password):
    '''账户验证'''

    # 获取用户信息
    # account_data={'account':'562500','password':'123456'}
    account_data = accounts.load_current_account(account)
    if account_data:
        if account_data['password'] == password:
            # 取改账户的过期时间，判断是否过去
            exp_time_sample = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d"))
            if exp_time_sample < time.time():
                print('您的卡：{}已过期!'.format(account))
                return
            else:
                return account_data
        else:
            print("\033[31m id or password is  incorrect \033[0m")


def acc_login(user_data, log_obj):
    '''账户登录'''
    retry_count = 0
    while retry_count < 3 and user_data['is_authenticated'] is not True:
        account = input('\033[32m you account:\33[0m').strip()
        password = input('\033[32m you password:\33[0m').strip()
        account_data = acc_auth(account, password)
        if account_data:
            log_obj.info('登录成功')
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            # user_data['account_data']=account_data
            return account_data
        else:
            retry_count += 1
    else:
        log_obj.error("account:{} 三次失败，退出程序".format(account))
        exit()
