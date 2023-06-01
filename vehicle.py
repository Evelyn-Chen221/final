'''
檔案名稱:vehicle.py
負責人:B11109050 洪熒孺
用途:繳納牌照稅及燃料稅相關功能(包含顯示信用卡、計算回饋)
'''

def calBonus1(tax):
    if tax > int(100/0.05 +2000/0.038):
        bonus = 2100
    elif tax <= 2000:
        bonus = int(tax * 0.05)
    else:
        bonus = int(tax * 0.05 + (tax - 2000) * 0.038)
    return bonus

def calBonus2(tax):
    if tax >= 2000:
        bonus = 100
    else: 
        bonus = int(tax * 0.05)
    return bonus

def calBonus3(tax):
    if tax > int(2000/0.038):
        bonus = 2000
    else:
        bonus = int(tax * 0.038)    
    return bonus

def calBonus4():
    bonus = 0
    return bonus

