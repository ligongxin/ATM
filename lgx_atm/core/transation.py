# _*_encoding=utf-8_*_
# 作者     :bozhong
# 创建时间 :2020/4/3012:40
# 文件     :
# IDE      :PyCharm
from lgx_atm.conf import settings


def make_transation(account_data, type, amount):
    amount = float(amount)
    if type in settings.TRANSATION_TYPE:
        interset = amount * settings.TRANSATION_TYPE[type]['interset']
        ole_balance = settings.TRANSATION_TYPE[type]['balance']
        if settings.TRANSATION_TYPE[type]['action'] == 'plus':
            new_balance = ole_balance + amount +interset
        elif settings.TRANSATION_TYPE[type]['action'] == 'mins':
            new_balance = ole_balance - amount - interset
        pass
    else:
        print('make_transation type is not exit!')
