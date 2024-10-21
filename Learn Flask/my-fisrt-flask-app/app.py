from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    my_name = "Jester"
    my_username = "mrjxtr"
    my_list = [1, 2, 5, 10, 20, 30]
    return render_template(
        "index.html", my_name=my_name, my_username=my_username, my_list=my_list
    )


@app.route("/other")
def other():
    return render_template("other.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5556, debug=True)
