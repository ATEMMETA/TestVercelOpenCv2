from flask import Flask, request, jsonify
import cv2

app = Flask(__name__)

@app.route('/test_opencv', methods=['POST'])
def test_opencv():
    try:
        dummy_image = cv2.imread('dummy.png')
        if dummy_image is not None:
            return jsonify({"status": "OpenCV imported successfully"})
        else:
            return jsonify({"status": "OpenCV imported, but couldn't read a dummy image (expected)"})
    except ImportError as e:
        return jsonify({"status": "ImportError", "error": str(e)})
    except Exception as e:
        return jsonify({"status": "Error", "error": str(e)})

@app.route('/test_get', methods=['GET'])
def test_get():
    return jsonify({"status": "GET request successful"})

if __name__ == '__main__':
    app.run(debug=True)
