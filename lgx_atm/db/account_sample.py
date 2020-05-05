# coding=gbk

import json

acc_dit = {
    'id': 1,
    'password': '123456',
    'credit': 15000,  # 额度
    'balance': 15000,  # 余额
    'enroll_date': '2016-01-02',  # 创建时间
    'expire_date': '2021-01-01',  # 过期时间
    'pay_day': 22,  # 还款日期
    'status': 0  # 0 = normal, 1 = locked, 2 = disabled  #状态，1，正常 2，锁了，3丢失
}

# print(json.dumps(acc_dit))

with open('accounts/1234.json', 'w') as f:
    f.write(json.dumps(acc_dit))
    f.close()
