from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    return 'this is Home page!'

from mod_admin import admin

app.register_blueprint(admin)