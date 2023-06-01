'''
檔案名稱:utility.py
負責人:B11109049 陳宜妏
用途:繳納水電費相關功能(包含顯示信用卡、計算回饋)
'''


def callBonus1(utility):
    if utility>int(1000/0.038):
        bonus=int(1000+(utility-int(1000/0.038))*0.001)
    else:
        bonus=int(utility*0.038)
    return bonus

def callBonus2(utility):
    if utility>int(200/0.01):
        bonus=200
    else:
        bonus=int(utility*0.01)
    return bonus

def callBonus3(utility):
    if utility>int(1000/0.038):
        bonus=1000
    else:
        bonus=int(utility*0.038)
    return bonus

def callBonus4():
    bonus = 0
    return bonus

