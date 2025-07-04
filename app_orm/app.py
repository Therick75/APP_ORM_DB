from flask import Flask, render_template, request, redirect, session, url_for
import requests
from utils import api_client
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form["correo"]
        password = request.form["password"]
        users = api_client.get_users()
        for user in users:
            if user["correo"] == correo:
                # Solo simulamos autenticación básica
                session["user"] = user
                return redirect(url_for("dashboard"))
        return render_template("login.html", error="Credenciales inválidas")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "correo": request.form["correo"],
            "password": request.form["password"]
        }
        api_client.create_user(data)
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/users", methods=["GET", "POST"])
def users():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "correo": request.form["correo"],
            "password": request.form["password"]
        }
        api_client.create_user(data)
        return redirect(url_for("users"))
    users = api_client.get_users()
    return render_template("users.html", users=users)

@app.route("/users/update/<int:user_id>", methods=["POST"])
def update_user(user_id):
    data = {
        "name": request.form["name"],
        "correo": request.form["correo"],
    }
    if request.form["password"]:
        data["password"] = request.form["password"]
    api_client.update_user(user_id, data)
    return redirect(url_for("users"))

@app.route("/users/delete/<int:user_id>")
def delete_user(user_id):
    api_client.delete_user(user_id)
    return redirect(url_for("users"))

@app.route("/categories", methods=["GET", "POST"])
def categories():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "userId": session["user"]["id"]
        }
        api_client.create_category(data)
        return redirect(url_for("categories"))
    categories = api_client.get_categories()
    return render_template("categories.html", categories=categories)

@app.route("/categories/update/<int:category_id>", methods=["POST"])
def update_category(category_id):
    data = {
        "name": request.form["name"]
    }
    api_client.update_category(category_id, data)
    return redirect(url_for("categories"))


@app.route("/categories/delete/<int:category_id>")
def delete_category(category_id):
    api_client.delete_category(category_id)
    return redirect(url_for("categories"))

# Rutas para products (mismo patrón que users y categories)
@app.route("/products", methods=["GET", "POST"])
def products():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "price": float(request.form["price"]),
            "Stock": int(request.form["Stock"]),
            "CategoryId": int(request.form["CategoryId"]),
            "userId": session["user"]["id"]
        }
        api_client.create_product(data)
        return redirect(url_for("products"))
    products = api_client.get_products()
    categories = api_client.get_categories()
    return render_template("products.html", products=products, categories=categories)

@app.route("/products/update/<int:product_id>", methods=["POST"])
def update_product(product_id):
    if "user" not in session:
        return redirect(url_for("login"))
    data = {
        "name": request.form["name"],
        "price": float(request.form["price"]),
        "Stock": int(request.form["Stock"]),
        "CategoryId": int(request.form["CategoryId"]),
        "userId": session["user"]["id"]
    }
    api_client.update_product(product_id, data)
    return redirect(url_for("products"))

@app.route("/products/delete/<int:product_id>")
def delete_product(product_id):
    if "user" not in session:
        return redirect(url_for("login"))
    api_client.delete_product(product_id)
    return redirect(url_for("products"))

if __name__ == "__main__":
    app.run(debug=True)
