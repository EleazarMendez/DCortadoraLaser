from flask import Blueprint, flash, g, redirect, render_template, request, Response
import face_recognition
import mediapipe as mp
import numpy as np
from .db import get_db
from .video import video, fotoToDB

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        matricula = request.form['matricula']
        correo = request.form['correo']
        movil = request.form['telefono']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        rol = request.form['rol'] # cambiar input cuando exista un S
        img = fotoToDB()
        try:
            db, c = get_db()
            c.execute(
                'INSERT INTO usuario (matricula, correo, telefono, nombre, apellido, rol, foto) VALUES(%s, %s, %s, %s, %s, %s, %s)', (matricula, correo, movil, nombre, apellido, rol, img.tobytes())
            )
            db.commit()
            db.close()
        except:
            return 'Error de conexión'
        return 'Datos enviados'
    return render_template('login/login.html')

@bp.route('/feed')
def feed():
    return Response(video(), mimetype="multipart/x-mixed-replace; boundary=frame")
