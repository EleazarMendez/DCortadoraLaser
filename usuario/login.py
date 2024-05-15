from flask import Blueprint, flash, g, redirect, render_template, request, Response
import cv2
import face_recognition
import mediapipe as mp
import numpy as np
from .db import get_db
from .video import video

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        return 'Formulario enviado'
    return render_template('login/login.html')

@bp.route('/feed')
def feed():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    return Response(video(cap,False), mimetype="multipart/x-mixed-replace; boundary=frame")
