from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/checkout", methods=["POST"])
def checkout():
    print(request.form)
<<<<<<< HEAD
    form_info = request.form
    print("This form request is printing from the checkout route", form_info)

    sum = (
        int(form_info["strawberry"])
        + int(form_info["raspberry"])
        + int(form_info["apple"])
    )

    print(f"Charging {form_info['first_name']} for {sum} fruits")

    return render_template("checkout.html", form_info=form_info)
=======
    form = request.form
    result = int(form["strawberry"]) + int(form["apple"]) + int(form["raspberry"])

    print(f"Charging {form['first_name']} for {result} fruits.")
    return render_template("checkout.html", form=form)
>>>>>>> e5015f45b15cf3c220c55459b14ad5e4c05f05a5


@app.route("/fruits")
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
