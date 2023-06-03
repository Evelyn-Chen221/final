'''
負責人:B11109050 洪熒孺
負責範圍: html檔案及python檔案修改為和html連結
用途:讓使用者更直覺操作系統
'''
'''
負責人:B11109046 徐名崴
負責範圍:主程式初步撰寫
'''
'''
負責人:B11109049 陳宜妏
負責範圍:html系統優化
用途:讓使用者在選擇離開時可以看到自己所選擇的稅種及費用還有分別的金額和會饋、美化離開介面、讓使用者可以返回上一頁、進行除錯設定
'''

from flask import Flask, render_template, request
import incometax
import calUtility
import vehicle
from flask import redirect, url_for



app = Flask(__name__)
#儲存稅種及費用的名稱
name_list=[]
#儲存稅種及費用的金額
money_list=[]
#儲存稅種及費用的會饋
bonus_list=[]
# 繳費系統首頁
@app.route("/")
def index():
    return render_template("index.html")

# 繳納綜合所得稅相關功能
@app.route("/income_tax", methods=["GET", "POST"])
def income_tax():
    if request.method == "POST":
        total_income_tax = float(request.form["amount"])
        payment_option = request.form["payment"]
        tax_money = int(incometax.calculate(total_income_tax))
        

        if payment_option == "建議方案":
            bonus = incometax.callTaxBonus1(tax_money)
        elif payment_option == "中信卡":
            bonus = incometax.callTaxBonus2(tax_money)
        elif payment_option == "匯豐卡":
            bonus = incometax.callTaxBonus3(tax_money)
        else:
            bonus = incometax.callTaxBonus4(tax_money)
        #將相關內容放進list中
        name_list.append("綜合所得稅")
        money_list.append(tax_money)
        bonus_list.append(bonus)
        return render_template("tax_result.html", name="綜合所得稅", bonus=bonus,tax_money=tax_money)
    
    else:
        if 'back' in request.args:
            return redirect(url_for('index'))
        return render_template("incometax.html", name="綜合所得稅", bonus=100)


# 繳納水電費相關功能
@app.route("/utility", methods=["GET", "POST"])
def utility():
    if request.method == "POST":
        payment_option = request.form["payment"]
        water_amount = int(request.form["water_amount"])
        electricity_amount = int(request.form["electricity_amount"])
        total = water_amount + electricity_amount

        if payment_option == "建議方案":
            bonus = calUtility.callBonus1(total)
        elif payment_option == "中信卡":
            bonus = calUtility.callBonus2(total)
        elif payment_option == "匯豐卡":
            bonus = calUtility.callBonus3(total)
        else:
            bonus = calUtility.callBonus4()
        #將相關內容放進list中
        name_list.append("水電費")
        money_list.append(total)
        bonus_list.append(bonus)
        return render_template("utility_result.html", name="水電費", bonus=bonus,utility_total=total)
    else:
        if 'back' in request.args:
            return redirect(url_for('index'))
        return render_template("utility.html", name="水電費", bonus=100, utility_total=0)
    
# 繳納牌照稅相關功能
@app.route("/vehicle_tax", methods=["GET", "POST"])
def vehicle_tax():
    if request.method == "POST":
        payment_option = request.form["payment"]
        tax = int(request.form["vehicle_amount"])
        if payment_option == "建議方案":
            bonus = vehicle.calBonus1(tax)
           
        elif payment_option == "玉山卡":
            bonus = vehicle.calBonus2(tax)
        elif payment_option == "台新卡":
            bonus = vehicle.calBonus3(tax)
        else:
            bonus = vehicle.calBonus4()
        #將相關內容放進list中
        name_list.append("牌照稅")
        money_list.append(tax)
        bonus_list.append(bonus)
        return render_template("tax_result.html", name="牌照稅", bonus=bonus,tax_money=tax)
    else:
        if 'back' in request.args:
            return redirect(url_for('index'))
        return render_template("vehicle.html", name="牌照稅", bonus=100)
    
# 繳納燃料稅相關功能
@app.route("/fuel_tax", methods=["GET", "POST"])
def fuel_tax():
    if request.method == "POST":
        payment_option = request.form["payment"]
        tax = int(request.form["fuel_amount"])
        if payment_option == "建議方案":
            bonus = vehicle.calBonus1(tax)
            
        elif payment_option == "玉山卡":
            bonus = vehicle.calBonus2(tax)
            
        elif payment_option == "台新卡":
            bonus = vehicle.calBonus3(tax)
           
        else:
            bonus = vehicle.calBonus4()
        #將相關內容放進list中
        name_list.append("燃料稅")
        money_list.append(tax)
        bonus_list.append(bonus)    
        return render_template("tax_result.html", name="燃料稅", bonus=bonus,tax_money=tax)
        
    else:
        if 'back' in request.args:
            return redirect(url_for('index'))
        return render_template("fuel.html", name="燃料稅", bonus=100)
    
@app.route("/leave", methods=["GET", "POST"])
def total():
    if request.method == "POST":
        # 使用者選擇離開，印出列表内容並返回
        print("名稱：", name_list)
        print("金額：",money_list)
        print("回饋：", bonus_list)
        return render_template("total_amount.html", name=name_list, money=money_list,bonus=bonus_list)
    elif request.method == "GET":
        # 使用者通過GET請求進入頁面，直接返回
        return render_template("total_amount.html", name=name_list, money=money_list,bonus=bonus_list)


if __name__ == "__main__":
    app.run(debug=True)
