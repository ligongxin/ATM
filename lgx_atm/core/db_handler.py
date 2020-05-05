# coding=gbk

from lgx_atm.conf import settings


def file_db_handler(db_conn):
    '''�ļ���ȡ'''
    file_path = "%s/%s" % (db_conn['path'], db_conn['name'])
    return file_path


def mysql_db_handler(db_conn):
    '''mysql��ȡ'''
    pass


# ��ȡ�ļ��ķ�ʽ
def db_handler():
    db_conn = settings.DATABASE
    if db_conn['engine'] == 'file_storage':
        return file_db_handler(db_conn)
    if db_conn['engine'] == 'mysql':
        return mysql_db_handler(db_conn)

# if __name__=='__main__':
# print(read_account(1))
