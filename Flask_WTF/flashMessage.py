from flask import Flask,render_template,request,redirect,flash,url_for
from flaskwtf import RegistrationForm

app=Flask(__name__)
app.secret_key="kliv_code"

@app.route("/", methods=["GET", "POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        flash(f"Welcome ,{name}! You Registred Succesfully", "success")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html")


if __name__=="__main__":
    app.run(debug=True)