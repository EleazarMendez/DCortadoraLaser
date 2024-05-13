from flask import Blueprint, flash, g, redirect, render_template, request

bp = Blueprint('home', __name__)

@bp.route('/', methods =['GET', 'POST'])
def home():
    if request.method == 'POST':
        return 'post'
    return render_template('home/home.html')
