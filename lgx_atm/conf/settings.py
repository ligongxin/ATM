# __author__:'lgx'
# date:2020/4/29 0029
import os,sys
#主路径
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#日志路径
log_path=os.path.join(BASE_DIR,'log')

#日志保存文件
LOG_FILE = {
    'account': "account.log",
    'transaction': "transaction.log"
}

#日志收集类型
LOG_TYPE='DEBUG'

#储存类型，file，db
DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': '%s/db' % BASE_DIR
}

TRANSATION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0},
    'withdraw': {'action': 'minus', 'interest': 0.05}

}



if __name__=="__main__":
    print(BASE_DIR)