from flask import Blueprint, flash, g, redirect, render_template, request, Response, url_for, session
import cv2
import functools
import mediapipe as mp
import numpy as np
from .db import get_db
from usuario.login import login_required

bp = Blueprint('userMenu', __name__, url_prefix='/userMenu')

@bp.route('/')
@login_required
def index():
    matricula = g.user['matricula']
    return render_template('accion/home.html')


