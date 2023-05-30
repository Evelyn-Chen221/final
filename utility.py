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
def calutilityBonus3():
    #utility水電費總金額
    water=int(input("請輸入您要繳的水費總額:"))
    power=int(input("請輸入您要繳的電費總額:"))
    utility=int(water+power)
    print("(1)  使用建議方案") 
    print("(2)  我只有國泰卡")
    print("(3)  我只有台新卡")
    print("(4)  我要用現金繳費")
    temp = int(input("請問要使用哪一種方案(請輸入數字)"))
    match temp:
        case 1:
            if utility>int(1000/0.038):
                bonus=int(1000+(utility-int(1000/0.038))*0.001)
            else:
                bonus=int(utility*0.038)
            return bonus
        case 2:
            if utility>int(200/0.01):
                bonus=200
            else:
                bonus=int(utility*0.01)
            return bonus
        case 3:
            if utility>int(1000/0.038):
                bonus=1000
            else:
                bonus=int(utility*0.038)
            return bonus
        case 4:
            bonus=0
            print("使用現金將無法獲得任何回饋。")
            return bonus
        case _:
            print("無此選項。")