# coding=gbk
from lgx_atm.core import accounts
from lgx_atm.db import account_sample
from lgx_atm.conf import settings


def creat_account():
    '''�����˻�'''
    creat_flag = True
    while creat_flag:
        account_id = input('����id:').strip()
        if len(account_id) > 0 and account_id.isdigit():
            acc_data = accounts.load_current_account(account_id)
            if acc_data:
                print('�˻��Ѵ���')
            else:
                account_sample.acc_dit['id'] = account_id
                account_sample.create_acc(account_id, account_sample.acc_dit)
                print('�����ɹ�')
        else:
            print('��������ȷ��id')
        if account_id == 'b':
            creat_flag = False


def suspend_account():
    '''��ʧ'''
    suspend_flag = True
    while suspend_flag:
        account_id = input('����id:').strip()
        if len(account_id) > 0 and account_id.isdigit():
            acc_data = accounts.load_current_account(account_id)
            if acc_data:
                acc_data['status'] = 2
                accounts.dump_account(acc_data)
                # account_sample.create_acc(account_id, account_sample.acc_dit)
                print('��ʧ�ɹ�')
            else:
                print('�˺Ų�����')

        else:
            print('��������ȷ��id')
        if account_id == 'b':
            suspend_flag = False


def lock_account():
    pass


def logout():
    pass


def run():
    '''�˻�����'''
    menu = u'''
        ------- manage Bank ---------
        \033[32;1m
        1.  �����˻�
        2.  ��ʧ
        3.  ����
        4.  ע��
        5.  �˳�
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
            print('��������ȷ��ָ��')


if __name__ == '__main__':
    run()
