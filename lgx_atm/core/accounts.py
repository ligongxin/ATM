# coding=gbk


from lgx_atm.conf import settings
from lgx_atm.core import db_handler
import json, os, sys


# 读取内容
def load_current_account(account):
    file_path = db_handler.db_handler()
    file_name = "%s\%s.json" % (file_path, account)

    # 判断是否为文件路径
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            account_data = json.loads(f.read())
            f.close()
            return account_data
    else:
        # print('账号不存在')
        return


# 更新内容
def dump_account(account):
    file_path = db_handler.db_handler()
    file_name = "%s\%s.json" % (file_path, account['id'])
    with open(file_name, 'w') as f:
        account_data = json.dump(account, f)
    return account_data
