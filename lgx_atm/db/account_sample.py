# coding=gbk

import json

acc_dit={
    'id':1234,
    'password':'123456',
    'credit':15000,  #���
    'balance':15000,  #���
     'enroll_date': '2016-01-02', #����ʱ��
    'expire_date': '2021-01-01',  #����ʱ��
    'pay_day': 22,  #��������
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled  #״̬��1������ 2�����ˣ�3��ʧ
}

# print(json.dumps(acc_dit))

with open('accounts/1234.json', 'w') as f:
    f.write(json.dumps(acc_dit))
    f.close()