'''
檔案名稱:utility.py
負責人:B11109049 陳宜妏
用途:繳納水電費相關功能(包含顯示信用卡、計算回饋)
'''


#showUtilityCard顯示可使用的信用卡
def showUtilitycard():
    print("    信用卡名稱        回饋比例     回饋上限")
    print("  國泰世華CUBE卡         1%          200")
    print("台新@GoGoCash御璽卡     3.8%         1000")
#calTaxBonus根據總稅額計算若使用上述三張信用卡可得的最大回饋
def calutilityBonus():
    utility=int(input("請輸入您要繳的水電費總額:"))
    if utility >26315:
        bonus=1000+(utility-26315)*0.01
    else:
        bonus=utility*0.038
    return bonus
