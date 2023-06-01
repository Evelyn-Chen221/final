'''
負責人:B11109050 洪熒孺
負責範圍: html檔案及python檔案修改為和html連結
用途:讓使用者更直覺操作系統
'''


from flask import Flask, render_template, request
import incometax
import calUtility
import vehicle

app = Flask(__name__)

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

        return render_template("tax_result.html", name="綜合所得稅", bonus=bonus,tax_money=tax_money)
    else:
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

        return render_template("utility_result.html", name="水電費", bonus=bonus,utility_total=total)
    else:
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

        return render_template("tax_result.html", name="牌照稅", bonus=bonus,tax_money=tax)
    else:
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

        return render_template("tax_result.html", name="燃料稅", bonus=bonus,tax_money=tax)
    else:
        return render_template("fuel.html", name="燃料稅", bonus=100)

if __name__ == "__main__":
    app.run(debug=True)
