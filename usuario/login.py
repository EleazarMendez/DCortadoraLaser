from flask import Blueprint, flash, g, redirect, render_template, request
import cv2
# import face_recognition
import mediapipe as mp
import numpy as np
from .db import get_db

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/')
def index():
    return 'Hola mundo'
