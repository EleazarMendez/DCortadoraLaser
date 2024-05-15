import cv2
import numpy as np
import face_recognition

def video(cap, foto):
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

                