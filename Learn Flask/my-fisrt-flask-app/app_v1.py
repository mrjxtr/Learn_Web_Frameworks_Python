"""
LEARNING HOW TO USE FLASK FRAMEWORK
"""

from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


# @app.route("hello", methods= ['GET', 'POST'])
@app.route("hello")
def hello():
    response = make_response("Hello World\n")
    response.status_code = 202
    response.headers["Content-Type"] = "test/plain"
    return response
    # if request.method == "GET":
    #     return "You made a GET request"
    # elif request.method == "POST":
    #     return "You made a POST request"
    # else:
    #     return "There is an error if you see this!"


@app.route("/greet/<name>", methods=["GET", "POST"])
def greet(name):
    return f"Hello {name}"


@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"


@app.route("/handle_params")
def handle_params():
    if "greeting" in request.args.key() and "name" in request.args.key():
        greeting = request.args["greeting"]
        name = request.args.get("name")
        return f"{greeting}, {name}"
    else:
        return "Error!: Some parameters are missing"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
