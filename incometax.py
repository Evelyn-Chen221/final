'''
檔案名稱:incometax.py
負責人:B11109049 陳宜妏
用途:繳納綜合所得稅相關功能(包含根據所得稅淨額計算總稅額、顯示信用卡、計算回饋)
'''
#total_income_tax為所得稅淨額
#tax_money為總稅額
#根據所得稅淨額計算總稅額
def calculate(total_income_tax):
    if total_income_tax <= 560000:
        tax_money = total_income_tax * 0.05
    elif total_income_tax >= 560001 and total_income_tax <= 1260000:
        tax_money = total_income_tax  * 0.12 - 39200
    elif total_income_tax >= 1260001 and total_income_tax <= 2520000:
        tax_money = total_income_tax* 0.2 - 140000
    elif total_income_tax >= 2520001 and total_income_tax <= 4720000:
        tax_money = total_income_tax* 0.3 - 392000
    else:
        tax_money = total_income_tax * 0.4 - 86400
    return tax_money


#根據推薦方案計算回饋
def callTaxBonus1(tax):
    if tax>50000:
        bonus=int(500+(tax-50000)*0.002)
    else:
        bonus=int(tax*0.01)
    return bonus
#只使用中信卡計算回饋
def callTaxBonus2(tax):
    bonus=int(tax*0.002)
    return bonus
#只使用匯豐卡計算回饋
def callTaxBonus3(tax):
    if tax>50000:
        bonus=500
    else:
        bonus=int(tax*0.01)
    return bonus
#使用現金
def callTaxBonus4(tax):
    bonus=0    
    return bonus
