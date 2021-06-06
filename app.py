#!python3

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    weight = ""
    height = ""
    bmi = ""
    if (
        request.method == "POST"
        and "html_weight" in request.form
        and "html_height" in request.form
    ):
        weight = float(request.form.get("html_weight"))
        height = float(request.form.get("html_height"))
        bmi = weight / (height * height)

    return render_template(
        "index.html", html_weight=weight, html_height=height, html_bmi=bmi
    )


app.run()
