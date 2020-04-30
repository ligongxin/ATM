# __author__:'lgx'
# date:2020/4/29 0029
import logging
from lgx_atm.conf import settings

def logger(log_type):
    logger=logging.getLogger(log_type) #日志名称
    logger.setLevel('DEBUG') #设置输出级别

    #创建屏幕输出
    ch=logging.StreamHandler()
    ch.setLevel(settings.LOG_TYPE) #设置输出级别

    #创建文件输出
    #日志路径
    log_file='%s\%s'%(settings.log_path,settings.LOG_FILE[log_type])
    fh=logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_TYPE)

    #输出信息
    formatter = logging.Formatter('%(asctime)s - %(filename)s -%(name)s - %(levelname)s -logmsg:%(message)s')

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

if __name__=='__main__':
    log_type='assount'
    logger=logger(log_type)
    logger.info('test')