# coding=gbk
from lgx_atm.core import accounts
from lgx_atm.db import account_sample
from lgx_atm.conf import settings


def creat_account():
    '''创建账户'''
    creat_flag = True
    while creat_flag:
        account_id = input('输入id:').strip()
        if len(account_id) > 0 and account_id.isdigit():
            acc_data = accounts.load_current_account(account_id)
            if acc_data:
                print('账户已存在')
            else:
                account_sample.acc_dit['id'] = account_id
                account_sample.create_acc(account_id, account_sample.acc_dit)
                print('创建成功')
        else:
            print('请输入正确的id')
        if account_id == 'b':
            creat_flag = False


def suspend_account():
    '''挂失'''
    suspend_flag = True
    while suspend_flag:
        account_id = input('输入id:').strip()
        if len(account_id) > 0 and account_id.isdigit():
            acc_data = accounts.load_current_account(account_id)
            if acc_data:
                acc_data['status'] = 2
                accounts.dump_account(acc_data)
                # account_sample.create_acc(account_id, account_sample.acc_dit)
                print('挂失成功')
            else:
                print('账号不存在')

        else:
            print('请输入正确的id')
        if account_id == 'b':
            suspend_flag = False


def lock_account():
    pass


def logout():
    pass


def run():
    '''账户管理'''
    menu = u'''
        ------- manage Bank ---------
        \033[32;1m
        1.  创建账户
        2.  挂失
        3.  锁卡
        4.  注销
        5.  退出
        \033[0m'''
    menu_dit = {
        '1': creat_account,
        '2': suspend_account,
        '3': lock_account,
        '5': logout,
    }
    print(menu)
    manage_flag = False
    while not manage_flag:
        user_input = input('>>:').strip()
        if user_input in menu_dit:
            menu_dit[user_input]()
        else:
            print('请输入正确的指令')


if __name__ == '__main__':
    run()
