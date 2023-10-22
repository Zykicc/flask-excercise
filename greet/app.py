from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome_page():
  return "WELCOME"

@app.route('/welcome/home')
def welcome_home_page():
  return "WELCOME HOME"

@app.route('/welcome/back')
def welcome_back_page():
  return "WELCOME BACK"