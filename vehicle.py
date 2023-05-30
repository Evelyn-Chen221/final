'''
檔案名稱:vehicle.py
負責人:B11109050 洪熒孺
用途:繳納牌照稅及燃料稅相關功能(包含顯示信用卡、計算回饋)
'''

def showCreditCard():
    print("     信用卡名稱        回饋比例     回饋上限")
    print("    玉山數位e卡          5%          100")
    print("台新@GoGoCash御璽卡     3.8%         2000")

def licenseMonitor():
    license =int(input("請輸入您要繳的牌照稅金額:"))
    return license

def fuelMonitor():
    fuel=int(input("請輸入您要繳的燃料稅金額:"))
    return fuel

def choose(tax):
    print("(1)  使用建議方案") 
    print("(2)  我只有玉山卡")
    print("(3)  我只有台新卡")
    print("(4)  我要用現金繳費")
    temp = int(input("請問要使用哪一種方案(請輸入數字)"))
    bonus = 0
    match temp:
        case 1:
            if tax > int(100/0.05 +2000/0.038):
                bonus = 2100
            elif tax <= 2000:
                bonus = int(tax * 0.05)
            else:
                bonus = int(tax * 0.05 + (tax - 2000) * 0.038)
            return bonus
        case 2:
            if tax > 2000:
                bonus = 100
            else: 
                bonus = int(tax * 0.05)
            return bonus
        case 3:
            if tax > int(2000/0.038):
                bonus = 2000
            else:
                bonus = int(tax * 0.038)    
            return bonus
        case 4:
            bonus = 0 
            print("使用現金將無法獲得任何回饋。")
            return bonus
        case _:
            print("無此選項。")
