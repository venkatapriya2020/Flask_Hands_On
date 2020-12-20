from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "<h1>Hello,World</h1>"



@app.route("/<string:fname>")
def hello(fname):
    fname=fname.capitalize()
    return f"Helloooooo,{fname}"
