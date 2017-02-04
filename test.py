from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def index ():
    return render_template("index.html")
@app.route("/about")
@app.route{"/about/<string:name>/<int:age>"}
def about(name = None):
    if name:
        return  {"emri": name, "mosha": age}
    else:
        return   "Hi there princess!"
if __name__== "__main__":
    app.run(debug=True)
