'''
檔案名稱:main.py
負責人:B11109046 徐名崴
用途:執行繳費系統的各種功能
'''

import incometax
import utility
import vehicle

#bonusList儲存回饋金額
#nameList儲存繳費名稱
bonusList = []*4
nameList = []*4

#繳費系統運作
while (True):
    
        #選擇繳費功能
        print("歡迎使用繳費系統！請選擇您需要的功能：")
        print("(1) 繳納綜合所得稅相關功能")
        print("(2) 繳納水電費相關功能")
        print("(3) 繳納牌照稅相關功能")
        print("(4) 繳納燃料稅相關功能")
        print("(0) 離開")
        
        choice = input("請輸入功能編號：")

        #對應所選繳費功能進行運算並將結果儲存至陣列
        match choice:
            case "1":
                total_income_tax = float(input("請輸入所得稅淨額："))
                tax_money = incometax.calculate(total_income_tax)
                print("總稅額為：", tax_money)
                incometax.showTaxcard()
                bonus = incometax.calTaxBonus(total_income_tax)
                bonusList.append(bonus)
                nameList.append("綜合所得稅")
            case "2":
                utility.showUtilitycard()
                bonus = utility.calutilityBonus3()
                bonusList.append(bonus)
                nameList.append("水電費")
            case "3":
                vehicle.showCreditCard()
                amount = vehicle.licenseMonitor()
                bonus = vehicle.choose(amount)
                bonusList.append(bonus)
                nameList.append("牌照稅")
            case "4":
                vehicle.showCreditCard()
                amount = vehicle.fuelMonitor()
                bonus=vehicle.choose(amount)
                bonusList.append(bonus)
                nameList.append("燃料稅")      
            case "0":
                print("名稱","      ","回饋金")
                for i in range(len(nameList)):
                    print(nameList[i],bonusList[i])
                print("感謝使用")
                break
            case _:
                print("無此選項。")
