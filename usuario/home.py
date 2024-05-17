from flask import Blueprint, flash, g, redirect, render_template, request, url_for

bp = Blueprint('home', __name__)

@bp.route('/', methods =['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('login.index'))
    return render_template('home/home.html')
