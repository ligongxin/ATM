# _*_encoding=utf-8_*_
# 作者     :bozhong
# 创建时间 :2020/4/3012:40
# 文件     :
# IDE      :PyCharm
from lgx_atm.conf import settings
from lgx_atm.core import accounts


def make_transaction(log_obj, account_data, type, amount, payer_id=0, *other):
    amount = float(amount)
    if type in settings.TRANSATION_TYPE:
        interest = amount * settings.TRANSATION_TYPE[type]['interest']
        old_balance = account_data['balance']
        old_credit = account_data['credit']
        # 转账
        if type == 'transfer':
            # 获取收款人的信息
            payer_account_data = accounts.load_current_account(payer_id)
            if payer_account_data:
                payer_old_credit = payer_account_data['credit']
                if old_credit > amount:
                    # 转账人的余额更新
                    new_credit = old_credit - amount
                    # 收款人余额更新,需要减去手续费
                    payer_new_credit = payer_old_credit + amount - interest
                    # 更新信息
                    account_data['credit'] = new_credit
                    payer_account_data['credit'] = payer_new_credit
                    accounts.dump_account(account_data)
                    accounts.dump_account(payer_account_data)
                    log_obj.info(
                        'account:{0},action:{1},amount:{2},interest:{3},payer_id:{4}'.format(account_data['id'],
                                                                                             settings.TRANSATION_TYPE[
                                                                                                 type][
                                                                                                 'action'],
                                                                                             amount, interest,
                                                                                             payer_id))
                    return account_data
                else:
                    print('账户余额不足，转账失败 ')
            # else:
            #     print('%s账户不存在' % payer_id)
            #     return
        # 还款，取款，
        else:

            if settings.TRANSATION_TYPE[type]['action'] == 'plus':
                new_balance = old_balance + amount + interest
            elif settings.TRANSATION_TYPE[type]['action'] == 'minus':
                new_balance = old_balance - amount - interest
                if new_balance < 0:
                    print('您的的额度不足，当前额度{0}，花费余额{1}，还缺少{2}'.format(old_balance, new_balance, new_balance - old_balance))
                    return
            # 更新账户额度
            account_data['balance'] = new_balance
            accounts.dump_account(account_data)
            log_obj.info('account:{0},action:{1},amount:{2},interest:{3}'.format(account_data['id'],
                                                                                 settings.TRANSATION_TYPE[type][
                                                                                     'action'],
                                                                                 amount, interest))
            return account_data
    else:
        print("\033[31;1mtransaction type[%s] is not exit!\033[0m" % type)
