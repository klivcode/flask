from flask import Flask,request,render_template,redirect,url_for,session,Response

app=Flask(__name__)
app.secret_key ="supersecret"


#Login page
@app.route("/", methods= ["GET", "POST"])
def login():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password =="123":
            session["user"] = username # store in session
            return redirect(url_for("welcome"))
        else:
            return Response("In-valid credentials. Try again", mimetype="text/pain") # text/HTML 
    return '''
        <h2>Login Page</h2>
            <form method ="POST">
                <label for="username"></label>
                <input type ="text" name="username"> <br>
                <label for="Password"></label>
                <input type ="text" name="password"> <br>
                <input type ="submit" value="Login">
            </form>
        '''


# Welcome Page after Login Page
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2> Welcome, {session["user"]}!<h2>
        <a href={url_for('logout')}>Logout</a>
        '''
    else:
        return redirect (url_for("login"))


#Logout route
@app.route("/logout")
def logout():
    session.pop("user",None) # session ['user']="Klivcode" None is help to overcome from the error if no user is available
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)