#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/3012:39
#文件     :
#IDE      :PyCharm

def acc_auth(account,password):
    '''账户验证'''

    # 获取用户信息
    account_data={'account':'562500','password':'123456'}
    if account_data['password'] == password:
        #取改账户的过期时间，判断是否过去
        pass



def acc_login():
    '''账户登录'''
    retry_count=0
    while retry_count < 0 :
        account=input('\033[32;you account:\33[0m').strip()
        password = input('\033[32;you password:\33[0m').strip()