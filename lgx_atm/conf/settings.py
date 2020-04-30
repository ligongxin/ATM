# __author__:'lgx'
# date:2020/4/29 0029
import os,sys
#主路径
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#日志路径
log_path=os.path.join(BASE_DIR,'log','log.txt')




if __name__=="__main__":
    print(BASE_DIR)