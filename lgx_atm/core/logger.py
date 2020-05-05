# __author__:'lgx'
# date:2020/4/29 0029
import logging, re
from lgx_atm.conf import settings


def logger(log_type):
    logger = logging.getLogger(log_type)  # 日志名称
    logger.setLevel(settings.LOG_TYPE)  # 设置输出级别

    # 创建屏幕输出
    ch = logging.StreamHandler()
    ch.setLevel('ERROR')  # 设置输出级别

    # 创建文件输出
    # 日志路径
    log_file = '%s\%s' % (settings.log_path, settings.LOG_FILE[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_TYPE)

    # 输出信息
    formatter = logging.Formatter('%(asctime)s - %(filename)s -%(name)s - %(levelname)s -logmsg:%(message)s')

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger


def pay_log(log_type):
    log_file = '%s\%s' % (settings.log_path, settings.LOG_FILE[log_type])
    with open(log_file, 'r') as f:
        log_data = f.readlines()
        # for i in log_data:
        #     if re.findall('1234',i):
        #         print(i)

        return log_data


if __name__ == '__main__':
    # log_type='assount'
    # logger=logger(log_type)
    # logger.info('test')
    acc_data = {'id': 1234}
    pay_log('transaction')
