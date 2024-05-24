from flask import Blueprint, flash, g, redirect, render_template, request, Response, url_for, session
import cv2
import functools
import mediapipe as mp
import numpy as np
from .db import get_db
from usuario.login import login_required
from .video import video, fotoToDB

bp = Blueprint('userMenu', __name__, url_prefix='/userMenu')

@bp.route('/')
@login_required
def index():
    matricula = g.user['matricula']
    return render_template('accion/userMain.html',usuario=matricula)

@bp.route('/noti',methods=['GET','POST'])
@login_required
def noti():
    db, c=get_db()
    matricula = g.user['matricula']
    c.execute('SELECT * FROM usuario WHERE matricula = %s', (matricula, ))
    user = c.fetchone()
    if request.method=='POST':
        correo=request.form['correo']
        telefono=request.form['telefono']
        notcorreo= True if request.form.get('notimail') == 'on' else False
        notmovil= True if request.form.get('noticel') == 'on' else False
        c.execute('UPDATE usuario SET correo = %s, telefono = %s, notcorreo = %s, notmovil = %s WHERE matricula = %s', (correo,telefono,notcorreo,notmovil,matricula))
        db.commit()
        return redirect(url_for('userMenu.index')) 
    return render_template('accion/noti.html', usuario=user)

@bp.route('/alta',methods=['GET','POST'])
@login_required
def altaUser():
    if request.method == 'POST':
        matricula = request.form['matricula']
        correo = request.form['correo']
        movil = request.form['telefono']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        rol = 'U'
        img = fotoToDB()
        db, c = get_db()
        c.execute(
            'INSERT INTO usuario (matricula, correo, telefono, nombre, apellido, rol, foto) VALUES(%s, %s, %s, %s, %s, %s, %s)', (matricula, correo, movil, nombre, apellido, rol, img.tobytes())
        )
        db.commit()
        return redirect(url_for('userMenu.index')) 
    return render_template(url_for('signin.index'))

@bp.route('/feed')
def feed():
    return Response(video(), mimetype="multipart/x-mixed-replace; boundary=frame")

