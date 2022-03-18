import os

from flask import Flask
from page_home import page_home
from page_download import page_download
from calc_stat import calc_stat
from calc_plot import calc_plot
from webhook import webhook

def create_app():

  app = Flask(__name__)
  app.config['GITHUB_SECRET'] = os.environ.get('GITHUB_SECRET')
  app.config['REPO_PATH'] = os.environ.get('REPO_PATH')
  app.register_blueprint(page_home)
  app.register_blueprint(page_download)
  app.register_blueprint(webhook)
  app.register_blueprint(calc_stat)
  app.register_blueprint(calc_plot)

  return(app)