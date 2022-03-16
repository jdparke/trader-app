import os

from flask import Flask
from homepage import homepage
from webhook import webhook

def create_app():

  app = Flask(__name__)
  app.config['GITHUB_SECRET'] = os.environ.get('GITHUB_SECRET')
  app.config['REPO_PATH'] = os.environ.get('REPO_PATH')
  app.register_blueprint(homepage)
  app.register_blueprint(webhook)

  return(app)