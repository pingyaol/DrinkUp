from flask import Flask, redirect, render_template,  request

waterfile = Flask(__name__)

@waterfile.route("/")
def index():
    return render_template("index.html")

@waterfile.route("/", methods=["Post"])
def index_post():
    frequency = request.form['Remind_Frequency']
    return redirect(request.referrer)


if __name__ == "__main__":
    waterfile.run(debug=True)