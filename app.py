from flask import Flask,render_template,Response,request,redirect
import cv2
import face_recognition
import numpy as np
#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime



app=Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///att.db'
#db = SQLAlchemy(app)

#class Att(db.Model):
#    roll=db.Column(db.String(9),primary_key=True)
 #   name=db.Column(db.String(20),nullable=False)
  #  email=db.Column(db.String(40),nullable=False)
   # encoding=db.Column(db.String())
    #def __repr__(self) -> str:
     #   return f'{self.roll} {self.name}'

def face_encodings(image):
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        return encode

def generate_frames(work=""):
    global camera
    camera=cv2.VideoCapture(0)
    while True:

        # read the camera frame
        success,frame=camera.read()
        frameS=cv2.resize(frame,(0,0),None,0.25,0.25)
        frameS=cv2.cvtColor(frameS,cv2.COLOR_BGR2RGB)

        face_curr_frame=face_recognition.face_locations(frameS)
        global encode_curr_frame
        encode_curr_frame=face_recognition.face_encodings(frameS,face_curr_frame)

        if  not success:
            break
        if len(face_curr_frame)==0:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            
            yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        else:
            for encode_face,faceloc in zip(encode_curr_frame,face_curr_frame):
                y1,x2,y2,x1=faceloc
                y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)

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
        return Response(generate_frames("take"),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/give_attendance')
def give_attendance():
    return render_template('give_att.html')

@app.route('/new_registration')
def new_registration():
    return render_template('new_regis.html')

@app.route('/reg_proceed',methods=['POST', 'GET'])
def reg_proceed():
    if request.method=='POST':
        message=False
        return render_template('reg_proceed.html',message=message) 

@app.route('/video_reg',methods=['POST', 'GET'])
def video_reg():
    if request.method=='POST':
        if len(encode_curr_frame)<1:
            print('redirected###################')
            camera.release()
            message=True
            return render_template('reg_proceed.html',message=message)
        a= encode_curr_frame[0]
        print("Face Encoding:",a)
        camera.release()
        return render_template('index.html',)
    else:
        return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/view_attendance')
def view_attendance():
    return render_template('view_attendance.html')

if __name__=='__main__':
    app.run(debug=True)

