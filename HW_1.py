from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def magazin():
    time_new=time.strftime('%H:%M:%S', time.localtime())
    contex={"title": "magazin",
            "content":"Вы находитесь на главной странице магазина одежды",
            "time": time_new,
            "telefon":88122744336}
    return render_template("index.html", **contex)

@app.route("/catalog.html/")
def catalog():
    contex={"title": "catalog",
            "cloth":"cloth.html",
            "hats":"/catalog/hats.html/",
            "shoes":"/catalog/shoes.html/",
            "telefon":88122744336}
    return render_template("catalog.html", **contex)

@app.route("/catalog.html/cloth.html/")
def cloth():
    contex={"title": "cloth",
            "telefon":88122744336}
    return render_template("cloth.html", **contex)

@app.route("/catalog/hats.html/")
def hats():
    contex={"title": "hats",
            "telefon":88122744336}
    return render_template("hats.html", **contex)

@app.route("/catalog/shoes.html/")
def shoes():
    contex={"title": "shoes",
            "telefon":88122744336}
    return render_template("shoes.html", **contex)

@app.route('/news.html/')
def news():
    time_new=time.strftime('%H:%M:%S %D', time.localtime())
    news=[{"news":"Погода Питера",
             "text":"В Питере вышло солнце. Люди радовались этому яркому кругу в небе",
             "time":"31.03.2024"},
            {"news": "Кот ученный",
             "text": "На дубе есть кот ученый, который ходит в лево и право и у него разные алгоритмы действий",
             "time": "01.04.2024"},
            {"news": "Домашние задание",
             "text": "Для проверки направлена работа по домашнему заданию",
             "time": time_new}]
    context={"cont": news}
    return render_template("news.html",**context)


if __name__=="__main__":
    app.run(debug=True)