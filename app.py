from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "nuuts-tulhuur"          # session-д хэрэгтэй, дурын үг

# Нэвтрэх эрхтэй хэрэглэгчид:  нэр: нууц үг
USERS = {"admin": "1234", "bat": "1111"}

# Бүтээгдэхүүний жагсаалт (шинийг нь энд нэмнэ)
PRODUCTS = [
    {"name": "Үхрийн мах",  "type": "Мал аж ахуй",    "price": "18,000₮ / кг", "icon": "🥩"},
    {"name": "Хонины мах",  "type": "Мал аж ахуй",    "price": "14,000₮ / кг", "icon": "🐑"},
    {"name": "Айраг",       "type": "Сүү, цагаан идээ", "price": "6,000₮ / л",   "icon": "🥛"},
    {"name": "Ааруул",      "type": "Сүү, цагаан идээ", "price": "12,000₮ / кг", "icon": "🧀"},
    {"name": "Төмс",        "type": "Газар тариалан", "price": "2,500₮ / кг",  "icon": "🥔"},
    {"name": "Лууван",      "type": "Газар тариалан", "price": "2,800₮ / кг",  "icon": "🥕"},
    {"name": "Улаан лооль", "type": "Хүлэмж",         "price": "7,000₮ / кг",  "icon": "🍅"},
    {"name": "Гурил",       "type": "Үр тариа",       "price": "3,200₮ / кг",  "icon": "🌾"},
]


@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS[:4])


@app.route("/products")
def products():
    return render_template("products.html", products=PRODUCTS)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        name = request.form["username"]
        if USERS.get(name) == request.form["password"]:
            session["user"] = name              # нэвтэрсэн гэж санана
            return redirect("/dashboard")
        error = "Нэвтрэх нэр эсвэл нууц үг буруу байна."
    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if "user" not in session:                   # нэвтрээгүй бол буцаана
        return redirect("/login")
    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
