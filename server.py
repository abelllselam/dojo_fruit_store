from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/checkout", methods=["POST"])
def checkout():
    print(request.form)
    form_info = request.form
    print("This form request is printing from the checkout route", form_info)

    sum = (
        int(form_info["strawberry"])
        + int(form_info["raspberry"])
        + int(form_info["apple"])
    )

    print(f"Charging {form_info['first_name']} for {sum} fruits")

    return render_template("checkout.html", form_info=form_info)


@app.route("/fruits")
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
