'''
檔案名稱:incometax.py
負責人:B11109049 陳宜妏
用途:繳納綜合所得稅相關功能(包含根據所得、顯示信用卡、計算回饋)
'''
#total_income_tax為所得稅淨額
#tax_money為總稅額
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
#showTaxCard顯示可使用的信用卡
def showTaxcard():
    print("     信用卡名稱　　　　回饋比例　　　回饋金上限")
    print("    中信Line pay　　　　0.2%　　　　    無")
    print("   匯豐銀行匯鑽卡　　　　 1%　　　　    500")
    print("台新@GoGoCash御璽卡     0.2%　　　　   2000")
#calTaxBonus根據總稅額計算若使用上述三張信用卡可得的最大回饋
def calTaxBonus():
    if calculate.tax_money >50000:
        bonus=500+(calculate.tax_money-50000)*0.002
    else:
        bonus=calculate.tax_money*0.01
    return bonus

