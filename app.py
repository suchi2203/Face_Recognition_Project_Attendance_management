from flask import Flask,render_template,Response,request
import cv2
import face_recognition
import numpy as np
#from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///att.db'
#db = SQLAlchemy(app)


def face_encodings(image):
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        return encode

def generate_frames():
    global camera
    camera=cv2.VideoCapture(0)
    while True:

        ## read the camera frame
        success,frame=camera.read()



        cv2.rectangle(frame,(0,0),(100,100),(0,255,0),2)
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')      

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video',methods=['POST', 'GET'])
def video():
    if request.method=='POST':
        camera.release()
        return render_template('index.html')
    else:
        return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/give_attendance')
def give_attendance():
    return render_template('give_att.html')

@app.route('/new_registration')
def new_registration():
    return render_template('new_regis.html')

@app.route('/view_attendance')
def view_attendance():
    return render_template('view_attendance.html')

if __name__=='__main__':
    app.run(debug=True)

