import os
import uuid

import pandas as pd
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
    Response,
    send_from_directory,
)

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def index():
    my_name = "Jester"
    my_username = "mrjxtr"
    # my_list = [1, 2, 5, 10, 20, 30]
    # return render_template(
    #     "index.html", my_name=my_name, my_username=my_username, my_list=my_list
    # )
    return render_template("index.html", my_name=my_name, my_username=my_username)


@app.route("/forms", methods=["GET", "POST"])
def forms():
    if request.method == "GET":
        return render_template("forms.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "mrjxtr" and password == "password":
            return redirect(url_for("index"))
        else:
            return "username or password incorrect"


@app.route("/upload_file", methods=["GET", "POST"])
def upload_file():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == "POST":
        uploaded_file = request.files["file"]

        if uploaded_file.content_type == "text/plain":
            return uploaded_file.read().decode()
        elif (
            uploaded_file.content_type
            == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            or uploaded_file.content_type == "application/vnd.sm-excel"
        ):
            df = pd.read_excel(uploaded_file)
            return df.to_html()


@app.route("/convert_csv", methods=["GET", "POST"])
def convert_csv():
    if request.method == "GET":
        return render_template("convert_csv.html")
    elif request.method == "POST":
        uploaded_file = request.files["file"]
        if (
            uploaded_file.content_type
            == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            or uploaded_file.content_type == "application/vnd.sm-excel"
        ):
            df = pd.read_excel(uploaded_file)
            response = Response(
                df.to_csv(),
                mimetype="text/csv",
                headers={"Content-Disposition": "attachment; filename=result.csv"},
            )

        return response


@app.route("/excel_to_csv", methods=["GET", "POST"])
def excel_to_csv():
    if request.method == "GET":
        return render_template("excel_to_csv.html")
    elif request.method == "POST":
        uploaded_file = request.files["file"]
        df = pd.read_excel(uploaded_file)
        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        filename = f"{uuid.uuid4()}.csv"
        df.to_csv(os.path.join("downloads", filename))

        return render_template("download_csv.html", filename=filename)


@app.route("/download/<filename>")
def download(filename):
    return send_from_directory("downloads", filename, download_name="results.csv")


@app.route("/other")
def other():
    return render_template("other.html")


@app.route("/redirect_endpoint")
def redirect_endpoint():
    return redirect(url_for("other"))


@app.route("/filters")
def filters():
    example_text = "Hello World"
    return render_template("filters.html", example_text=example_text)


@app.template_filter("reverse_string")
def reverse_string(s):
    return s[::-1]


@app.template_filter("repeat")
def repeat(s, times=3):
    return s * times


@app.template_filter("alternate_case")
def alternate_case(s):
    return "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5556, debug=True)
