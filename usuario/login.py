from flask import Blueprint, flash, g, redirect, render_template, request, Response
import cv2
import face_recognition
import mediapipe as mp
import numpy as np
from .db import get_db
from .video import video, fotoToDB

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        path = fotoToDB('Eleazar')
        try:
            image = path.tobytes()
            img = str(image)
            return img
        except:
            return 'No se pudo'
    return render_template('login/login.html')

@bp.route('/feed')
def feed():
    return Response(video(), mimetype="multipart/x-mixed-replace; boundary=frame")
