from flask import Flask,render_template,request

app=Flask(__name__)


@app.route("/feedback", methods=["POST","GET"])
def feedback():
    if request.method=="POST":
        name= request.form.get("username") # return none id if username is missing
        message=request.form.get("message")
        
        return render_template ("thankyou.html", user=name, message=message)
    
    
    return render_template("feedback.html")

if __name__=="__main__":
    app.run(debug=True)