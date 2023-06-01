from flask import Flask, render_template

app = Flask(__name__)

# 繳費系統首頁
@app.route("/")
def index():
    return render_template("index.html")

# 繳納綜合所得稅相關功能
@app.route("/income_tax")
def income_tax():
    # 實現繳納綜合所得稅的相關功能
    # ...
    return render_template("result.html", name="綜合所得稅", bonus=100)

# 繳納水電費相關功能
@app.route("/utility_bill")
def utility_bill():
    # 實現繳納水電費的相關功能
    # ...
    return render_template("result.html", name="水電費", bonus=200)

# 繳納牌照稅相關功能
@app.route("/vehicle_tax")
def vehicle_tax():
    # 實現繳納牌照稅的相關功能
    # ...
    return render_template("result.html", name="牌照稅", bonus=300)

# 繳納燃料稅相關功能
@app.route("/fuel_tax")
def fuel_tax():
    # 實現繳納燃料稅的相關功能
    # ...
    return render_template("result.html", name="燃料稅", bonus=400)

# 使用完畢離開
@app.route("/leave")
def leave():
    return render_template("leave.html")

if __name__ == "__main__":
    app.run(debug=True)
