# coding=gbk
from lgx_atm.conf import settings
import json,os,sys

def read_account(account):
    file_name="%s\db\%s.json"%(settings.BASE_DIR,account)
    #�ж��Ƿ�Ϊ�ļ�·��
    if os.path.isfile(file_name):
        with open(file_name,'r') as f:
            account_data=json.loads(f.read())
            f.close()
            return account_data
    else:
        print('�˺Ų�����')
        return
#��ȡ�ļ��ķ�ʽ
def db_handler():
    pass


if __name__=='__main__':
    print(read_account(1))
