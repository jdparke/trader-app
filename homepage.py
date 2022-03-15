from flask import Blueprint

homepage = Blueprint('homepage', __name__)

@homepage.route('/')
def index():
    return "<h1>Parker's Trader app NEW 3!!!</h1>"