from flask import Flask
app = Flask(_name_)
@app.route("/")
def hello_world():
    return "Hello, World!"
if_name_=="_main_":
app.run(host="0.0.0.0", port=8080)
@app.route("/about")
def about():
    return "This is the About page."
