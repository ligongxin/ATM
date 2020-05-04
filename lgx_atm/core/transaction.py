# _*_encoding=utf-8_*_
# 作者     :bozhong
# 创建时间 :2020/4/3012:40
# 文件     :
# IDE      :PyCharm
from lgx_atm.conf import settings
from lgx_atm.core import accounts


def make_transaction(log_obf, account_data, type, amount):
    amount = float(amount)
    if type in settings.TRANSATION_TYPE:
        interest = amount * settings.TRANSATION_TYPE[type]['interest']
        ole_balance = account_data['balance']
        if settings.TRANSATION_TYPE[type]['action'] == 'plus':
            new_balance = ole_balance + amount + interest
        elif settings.TRANSATION_TYPE[type]['action'] == 'mins':
            new_balance = ole_balance - amount - interest
            if new_balance < 0:
                print('您的的额度不足，当前额度{0}，花费余额{1}，还缺少{2}'.format(ole_balance, new_balance, new_balance - ole_balance))
                return
        # 更新账户额度
        account_data['balance'] = new_balance
        accounts.dump_account(account_data)
        log_obf.info('account:{0},action:{1},amount:{2},interest:{3}'.format(account_data['id'],
                                                                             settings.TRANSATION_TYPE[type]['action'],
                                                                             amount, interest))
        return new_balance
    else:
        print("\033[31;1mtransaction type[%s] is not exit!\033[0m" % type)
