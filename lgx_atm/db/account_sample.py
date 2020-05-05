# coding=gbk

import json
from lgx_atm.conf import settings
from lgx_atm.core import db_handler

acc_dit = {
    'id': 1,
    'password': '123456',
    'credit': 15000,  # 额度
    'balance': 15000,  # 余额
    'enroll_date': '2016-01-02',  # 创建时间
    'expire_date': '2021-01-01',  # 过期时间
    'pay_day': 22,  # 还款日期
    'status': 0  # 0 = normal, 1 = locked, 2 = disabled  #状态，0，正常 1，锁了，2丢失
}


# print(json.dumps(acc_dit))

def create_acc(account_id, acc_dit):
    file_path = db_handler.db_handler()
    file_name = '%s\%s.json' % (file_path, account_id)
    with open(file_name, 'w') as f:
        f.write(json.dumps(acc_dit))
        f.close()
