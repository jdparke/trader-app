from flask import Blueprint, render_template

homepage = Blueprint('homepage', __name__)

@homepage.route('/')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)