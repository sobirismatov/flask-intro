from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
   return "<hi>Hello World!</hi>"
@app.route("/about")
def about():
   return "<hi>About Page!</hi>"

if __name__ == "__main__":
   app.run(port=None)
