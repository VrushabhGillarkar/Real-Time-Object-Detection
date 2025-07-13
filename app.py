from flask import Flask, render_template, Response, jsonify
from detect import detect_objects, detected_objects_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(detect_objects(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/detection_data')
def detection_data():
    return jsonify(detected_objects_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)