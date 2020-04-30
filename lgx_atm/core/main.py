#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/3012:40
#文件     :
#IDE      :PyCharm
from lgx_atm.core import logger
from lgx_atm.core import auth

#user_data,记住用户是否登录
user_data={
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

# def interactive():

# 主流程，用户登录 auth_login
#定义日志
account_logger=logger.logger('account')  #账户日志


def run():
    auth.acc_login(user_data,account_logger)


if __name__=='__main__':
    run()