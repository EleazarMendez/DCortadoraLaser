from flask import Blueprint, flash, g, redirect, render_template, request, Response, url_for, session
import cv2
import functools
import numpy as np
from .db import get_db
from .video import fotoaut, detection

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        db,c=get_db()
        c.execute('SELECT matricula,foto FROM usuario')
        usuarios=c.fetchall()
        matricula=[]
        foto=[]
        for usuario in usuarios:
            matricula.append(usuario['matricula'])
            img_db=usuario['foto']
            img_bytes=np.frombuffer(img_db, dtype=np.uint8)
            img=cv2.imdecode(img_bytes, cv2.IMREAD_COLOR)
            foto.append(img)
        user=fotoaut(matricula, foto)
        if user in matricula:
            session.clear()
            session['user_id'] = user
            return redirect(url_for('userMenu.index'))
        else:
            error = 'Usuario no registrado'
            flash(error)
    return render_template('login/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.home'))

@bp.route('/feed')
def feed():
    db, c = get_db()
    c.execute('SELECT foto FROM usuario')
    usuarios=c.fetchall()
    matricula=[]
    foto=[]
    for usuario in usuarios:
        img_db=usuario['foto']
        img_bytes=np.frombuffer(img_db, dtype=np.uint8)
        img=cv2.imdecode(img_bytes, cv2.IMREAD_COLOR)
        foto.append(img)
    return Response(detection(foto), mimetype="multipart/x-mixed-replace; boundary=frame")

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        db, c = get_db()
        c.execute('SELECT * FROM usuario WHERE matricula = %s', (user_id, ))
        g.user = c.fetchone()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('home.home'))
        return view(**kwargs)
    return wrapped_view