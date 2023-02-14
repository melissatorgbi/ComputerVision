from flask import Flask,render_template,Response

from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)



app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        # Use the model
        #source=0 for webcam but can deal with image files and folders as well
        results = model.predict(source="0" ,show=False, box=True)  
        print(results)  
        
        ## read the camera frame
        #success,frame=camera.read()
        #if not success:
        #    break
        #else:
        #    ret,buffer=cv2.imencode('.jpg',frame)
        #    frame=buffer.tobytes()

        #yield(b'--frame\r\n'
        #           b'Content-Type image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)