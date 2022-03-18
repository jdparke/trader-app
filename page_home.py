from flask import Blueprint, render_template

page_home = Blueprint('page_home', __name__)

@page_home.route('/')
def index():
    return render_template('page_home.html', title='Home')