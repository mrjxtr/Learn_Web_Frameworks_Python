from flask import Flask, render_template, session, make_response, request, flash


app = Flask(__name__, template_folder="templates")
app.secret_key = "JUST A RANDOM KEY"


@app.route("/")
def index():
    return render_template("index.html", message="Index")


@app.route("/set_session")
def set_session():
    session["name"] = "Jester"
    session["user"] = "mrjxtr"
    return render_template("index.html", message="Session set")


@app.route("/get_session")
def get_session():
    name = session["name"]
    user = session["user"]
    return render_template("index.html", message=f"Name: {name}, Session: {user}")


@app.route("/clear_session")
def clear_session():
    session.clear()
    return render_template("index.html", message="Session cleared")


@app.route("/set_cookie")
def set_cookie():
    response = make_response(render_template("index.html", message="Cookies set"))
    response.set_cookie("cookie_name", "cookie_value")
    return response


@app.route("/get_cookie")
def get_cookie():
    cookie_value = request.cookies["cookie_name"]
    return render_template("index.html", message=f"Cookie_value: {cookie_value}")


@app.route("/clear_cookie")
def clear_cookie():
    response = make_response(render_template("index.html", message="Cookies cleared"))
    response.set_cookie("cookie_name", expires=0)
    return response


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "mrjxtr" and password == "12345":
            flash("Successful Login!")
            return render_template("index.html", message="")
        else:
            flash("Login Failed!")
            return render_template("login.html", message="")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
