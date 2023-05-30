'''
檔案名稱:vehicle.py
負責人:B11109050 洪熒孺
用途:繳納牌照稅及燃料稅相關功能(包含顯示信用卡、計算回饋)
'''

def showCreditCard():
    print("     信用卡名稱        回饋比例     回饋上限")
    print("    玉山數位e卡          5%          100")
    print("台新@GoGoCash御璽卡     3.8%         2000")

def monitor():
    license =int(input("請輸入您要繳的牌照稅金額:"))
    fuel=int(input("請輸入您要繳的燃料稅金額:"))
    amount = int(license + fuel)
    return amount

def choose():
    print("(1)  使用建議方案") 
    print("(2)  我只有玉山卡")
    print("(3)  我只有台新卡")
    print("(4)  我要用現金繳費")
    temp = input("請問要使用哪一種方案(請輸入數字)")
    total = monitor.amount
    bonus = 0
    match temp:
        case 1:
            if total > int(100/0.05 +2000/0.038):
                bonus = 2100
            elif total <= 2000:
                bonus = int(total * 0.05)
            else:
                bonus = int(total * 0.05 + (total - 2000) * 0.038)
        case 2:
            if total > 2000:
                bonus = 100
            else: 
                bonus = int(total * 0.05)
        case 3:
            if total > int(2000/0.038):
                bonus = 2000
            else:
                bonus = int(total * 0.038)    
        case 4:
            bonus = 0 #未來要寫問使用者是否確定使用現金
        case _:
            print("無此選項。")
