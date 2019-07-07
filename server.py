from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "not very a secret"

@app.route("/")
def index():
    session['number'] = int(random.random()*100)
    return render_template("index.html")

@app.route("/gues", methods = ["POST"])
def gues():
    if int(request.form["number"]) < session["number"]:
        session["answer"] = "Too Low :("
    elif int(request.form["number"]) > session["number"]:
        session["answer"] = "Too Hight :("
    else:
        session["answer"] = "correct!"
    return redirect("/gues_again")

@app.route("/gues_again")
def gues_again():
    if session["answer"] == "correct!":
        return render_template("correct.html", number=session["number"])
    else:
        return render_template("index.html", answer = session["answer"])




#------------------------
if __name__ == "__main__":
    app.run(debug=True)