from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'I am a chosen one Server works'

@app.route('/chosen')
def chosen():
  return 'Chosen never die, we will live and praise the lord'
