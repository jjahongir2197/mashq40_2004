@app.route("/age35", methods=["GET", "POST"])
def age35():

    if request.method == "POST":

        surname = request.form.get("surname")
        age = request.form.get("age")

        return render_template(
            "result35.html",
            surname=surname,
            age=age
        )

    return render_template("index35.html")
