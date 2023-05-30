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
#calTaxBonus根據總稅額計算若使用上述三張信用卡可得的最大回饋
def calTaxBonus():
    print("(1)  使用建議方案") 
    print("(2)  我只有中信卡")
    print("(3)  我只有匯豐卡")
    print("(4)  我要用現金繳費")
    temp = input("請問要使用哪一種方案(請輸入數字)")
    match temp:
        case 1:
            if calculate.tax_money>50000:
                bonus=int(500+(calculate.tax_money-50000)*0.002)
            else:
                bonus=int(calculate.tax_money*0.01)
        case 2:
            bonus=int(calculate.tax_money*0.002)
        case 3:
            if calculate.tax_money>50000:
                bonus=500
            else:
                bonus=int(calculate.tax_money*0.01)
        case 4:
            bonus=0
        case _:
            print("無此選項。")

