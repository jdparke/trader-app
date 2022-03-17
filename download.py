from flask import Blueprint, render_template

download = Blueprint('download', __name__)

@download.route('/download')
def get_download():
    return render_template('download.html', title='Download Stocks')