from flask import Flask,render_template, request

import marks

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def money():
    # print("aayush",request.method,request.form["hrs"])
    if request.method == "POST":
        # print("ddd")
        hrs = request.form["hrs"]
        money_pred = marks.do_predict(hrs)
        mk = money_pred
        return render_template("index.html",my_marks = mk)
    return render_template("index.html")

# @app.route("/sub",methods=["POST"])
# def submit():
#     #html -> .py
#     if request.method=="POST":
#         name = request.form["username"]

#     #.py->html
#     return render_template("sub.html",n=name)

if __name__ == "__main__":
    app.run(debug=True)