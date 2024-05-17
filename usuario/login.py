from flask import Blueprint, flash, g, redirect, render_template, request, Response
import cv2
import face_recognition
import mediapipe as mp
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
            return user
        else:
            return 'Quien chota sos?'  
    return render_template('login/login.html')

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

