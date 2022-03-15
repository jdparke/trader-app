from flask import Flask
from homepage import homepage
from webhook import webhook

app = Flask(__name__)
app.register_blueprint(homepage)
app.register_blueprint(webhook)