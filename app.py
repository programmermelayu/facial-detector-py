import os
import cv2
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS # Required for cross-origin requests if running frontend separately
import base64
import random # For placeholder expression

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Define the path to the Haar Cascade XML file
# Ensure 'haarcascade_frontalface_default.xml' is in the same directory as app.py
HAARCASCADE_PATH = os.path.join(os.path.dirname(__file__), 'haarcascade_frontalface_default.xml')

# Load the Haar Cascade classifier for face detection
try:
    face_cascade = cv2.CascadeClassifier(HAARCASCADE_PATH)
    if face_cascade.empty():
        raise IOError(f"Could not load Haar Cascade classifier from {HAARCASCADE_PATH}")
    print(f"Successfully loaded Haar Cascade classifier from {HAARCASCADE_PATH}")
except IOError as e:
    print(f"Error loading Haar Cascade: {e}")
    print("Please ensure 'haarcascade_frontalface_default.xml' is in the same directory as 'app.py'")
    face_cascade = None # Set to None to handle gracefully if loading fails

# --- Placeholder for Expression Detection Logic ---
# In a real application, you would load a pre-trained deep learning model here
# For example, using TensorFlow/Keras or a pre-trained OpenCV DNN model.
#
# Example (conceptual, requires model files):
# emotion_model = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'weights.caffemodel')
# EMOTIONS = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
#
def detect_expression_placeholder(face_roi):
    """
    Placeholder function for facial expression detection.
    In a real application, this would use a machine learning model.
    For this example, it returns a random expression.
    """
    expressions = ["Happy", "Sad", "Neutral", "Surprise", "Angry"]
    return random.choice(expressions)

# Route to serve the HTML page
@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

# Route to handle facial expression analysis
@app.route('/analyze', methods=['POST'])
def analyze_facial_expression():
    """
    Receives an image (base64 encoded), detects faces, and
    returns a placeholder facial expression.
    """
    if not face_cascade:
        return jsonify({"error": "Face detection model not loaded. Check server logs."}), 500

    data = request.json
    if 'imageData' not in data:
        return jsonify({"error": "No imageData provided"}), 400

    # Extract base64 string and remove the "data:image/jpeg;base64," prefix
    base64_image = data['imageData'].split(',')[1]

    try:
        # Decode base64 string to bytes
        image_bytes = base64.b64decode(base64_image)
        # Convert bytes to a NumPy array
        np_arr = np.frombuffer(image_bytes, np.uint8)
        # Decode NumPy array to OpenCV image
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if frame is None:
            return jsonify({"error": "Could not decode image"}), 400

        # Convert to grayscale for face detection (Haar Cascades work better with grayscale)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        # Parameters: image, scaleFactor, minNeighbors, minSize
        faces = face_cascade.detectMultiScale(gray_frame, 1.1, 4, minSize=(100, 100)) # Increased minSize for better detection

        if len(faces) > 0:
            # For simplicity, we'll analyze the first detected face
            (x, y, w, h) = faces[0]
            face_roi = gray_frame[y:y+h, x:x+w] # Region of Interest for the face

            # Call the placeholder expression detection
            expression = detect_expression_placeholder(face_roi)
            return jsonify({"expression": expression, "face_detected": True})
        else:
            return jsonify({"expression": "No face detected", "face_detected": False})

    except Exception as e:
        print(f"Error during analysis: {e}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask app
    # host='0.0.0.0' makes it accessible from other devices on the network
    # debug=True enables debug mode (reloads on code changes, shows errors)
    app.run(host='0.0.0.0', port=5000, debug=True)

