import cv2
import numpy as np
import face_recognition

def video():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        face_locations = face_recognition.face_locations(frame)
        if ret:
            if face_locations != []:
                for face_location in face_locations:
                    cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), (0, 255, 0))
                (flag, encodeImage) = cv2.imencode('.jpg', frame)
                if not flag:
                    continue
                yield(b'--frame\r\n' b'content-Type: image/jpeg\r\n\r\n'+bytearray(encodeImage)+b'\r\n')
        else:
            continue


def fotoToDB():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    _, image_bytes = cv2.imencode('.jpg', frame)
    return image_bytes

def detection(fotos):
    facesEncodings=[]
    for foto in fotos:
        face_loc=face_recognition.face_locations(foto)[0]
        f_coding=face_recognition.face_encodings(foto,known_face_locations=[face_loc])[0]
        facesEncodings.append(f_coding)
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    while True:
        ret, frame=cap.read()
        if ret==False: break
        frame=cv2.flip(frame,1)
        face_locations=face_recognition.face_locations(frame)
        if face_locations != []:
            for face_location in face_locations:
                face_frame_encodings=face_recognition.face_encodings(frame,known_face_locations=[face_location])[0]
                result = face_recognition.compare_faces(facesEncodings,face_frame_encodings)
            if True in result:
                color=(0,255,0)
            else:
                color=(0,0,255)
            cv2.rectangle(frame,(face_location[3],face_location[0]),(face_location[1],face_location[2]),color,2)
        (flag, encodeImage) = cv2.imencode('.jpg', frame)
        if not flag:
            continue
        yield(b'--frame\r\n' b'content-Type: image/jpeg\r\n\r\n'+bytearray(encodeImage)+b'\r\n')

def fotoaut(matriculas,fotos):
    facesEncodings=[]
    try:
        for foto in fotos:
            face_loc=face_recognition.face_locations(foto)[0]
            f_coding=face_recognition.face_encodings(foto,known_face_locations=[face_loc])[0]
            facesEncodings.append(f_coding)
        cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        face_locations=face_recognition.face_locations(frame)
        if face_locations != []:
            for face_location in face_locations:
                face_frame_encodings=face_recognition.face_encodings(frame,known_face_locations=[face_location])[0]
                result = face_recognition.compare_faces(facesEncodings,face_frame_encodings)
                if True in result:
                    index = result.index(True)
                    matricula = matriculas[index]
                else: 
                    matricula = 'Desconocido'
        return matricula
    except:
        return 'no detection'



