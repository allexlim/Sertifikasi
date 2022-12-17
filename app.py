from flask import Flask # untuk import flask
from flask import render_template as rt

app = Flask(__name__)

@app.route('/')
def main():
    return rt("pilihan.html")

if __name__ == "__main__":
  app.run(debug=True)