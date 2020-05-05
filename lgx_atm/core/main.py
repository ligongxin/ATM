# _*_encoding=utf-8_*_
# 作者     :bozhong
# 创建时间 :2020/4/3012:40
# 文件     :
# IDE      :PyCharm
from lgx_atm.core import logger
from lgx_atm.core import auth, accounts, transaction
import re
from lgx_atm.core.auth import login_required

# user_data,记住用户是否登录
user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}

# 主流程，用户登录 auth_login
# 定义日志
account_logger = logger.logger('account')  # 账户日志
transaction_logger = logger.logger('transaction')  # 交易记录


@login_required
def account_info(acc_data):
    '''账户信息'''
    acc_info = '''------------- BALANCE INFO ---------------
    卡号:{0}
    余额:{1}
    额度:{2}
    过期时间:{3}
    还款日:{4}
    '''.format(acc_data['id'], acc_data['credit'], acc_data['balance'], acc_data['expire_date'], acc_data['pay_day'])
    print(acc_info)


@login_required
def repay(acc_data):
    '''还款'''
    # 获取最新的数据
    new_account_data = accounts.load_current_account(acc_data['account_id'])
    current_balance = '''------------- BALANCE INFO ---------------
    Credit:{0}元
    Balance:{1}元'''.format(new_account_data['credit'], new_account_data['balance'])
    print(current_balance)
    # 进行还款操作
    repay_flag = True
    while repay_flag:
        repay_amount = input('\033[33;1mInput repay amount:\33[0m').strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            new_balance = transaction.make_transaction(transaction_logger, new_account_data, 'repay', repay_amount)
            if new_balance:
                print('new_balance:%s' % new_balance['balance'])
        else:
            print('repay amount is valid,')
        if repay_amount == 'b':
            repay_flag = False


@login_required
def withdraw(acc_data):
    '''取款'''
    # 获取最新的数据
    new_account_data = accounts.load_current_account(acc_data['account_id'])
    current_balance = '''------------- BALANCE INFO ---------------
        Credit:{0}元
        Balance:{1}元'''.format(new_account_data['credit'], new_account_data['balance'])
    print(current_balance)
    # 进行存款操作
    withdraw_flag = True
    while withdraw_flag:
        withdraw_amount = input('\033[33;1mInput withdraw amount:\33[0m').strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(transaction_logger, new_account_data, 'withdraw',
                                                       withdraw_amount)
            print('new balance:%s' % new_balance['balance'])
        else:
            print('withdraw amount is valid')
        if withdraw_amount == 'b':
            withdraw_flag = False


@login_required
def transfer(acc_data):
    '''转账'''
    # 获取最新的数据
    new_account_data = accounts.load_current_account(acc_data['account_id'])
    current_balance = '''------------- BALANCE INFO ---------------
            Credit:{0}元
            Balance:{1}元'''.format(new_account_data['credit'], new_account_data['balance'])
    print(current_balance)
    # 转账
    transfer_flag = True
    while transfer_flag:
        payer_id = input('需要转账的卡号：').strip()
        if len(payer_id) > 0:
            # 获取转账人的账户信息
            transfer_amount = input('请输入转账金额：').strip()
            if len(transfer_amount) > 0 and transfer_amount.isdigit():
                new_credit = transaction.make_transaction(transaction_logger, new_account_data, 'transfer',
                                                          transfer_amount,
                                                          payer_id)
                if new_credit:
                    print('new credit:%s' % new_credit['credit'])
            else:
                print('请输入正确的金额')
            if payer_id == 'b':
                transfer_flag = False
        else:
            print('请输入正确的账号')


@login_required
def pay_check(acc_data):
    # 读取日志
    # 日志路径
    log_data = logger.pay_log('transaction')
    for i in log_data:
        if re.findall(str(acc_data['account_id']), i):
            print(i)


@login_required
def logout(acc_data):
    print('Welcome to come again!')
    exit()


def interactive(acc_data):
    '''业务菜单'''
    menu = u'''
    ------- Oldboy Bank ---------
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout
    }
    exit_fiag = False
    while not exit_fiag:
        print(menu)
        user_option = input('>>:').strip()
        if user_option in menu_dic:
            # print('accdata:%s' % acc_data)
            # 执行对应的业务
            menu_dic[user_option](acc_data)
        else:
            print('"\033[31;1mOption does not exist!\033[0m"')


def run():
    # 用户登录
    acc_data = auth.acc_login(user_data, account_logger)
    # 展示业务菜单
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)


if __name__ == '__main__':
    run()

    # accdata = {'id': 1234, 'password': '123456', 'credit': 9000.0, 'balance': 15000, 'enroll_date': '2016-01-02',
    #            'expire_date': '2021-01-01', 'pay_day': 22, 'status': 0}
    #
    # transfer(accdata)
