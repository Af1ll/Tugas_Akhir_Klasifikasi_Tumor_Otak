import os
from flask import Blueprint, request, jsonify, current_app, render_template
from werkzeug.utils import secure_filename
from app.utils import allowed_file
from app.model_service import predict

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@main.route('/predict', methods=['GET'])
def predict_page():
    return render_template('predict.html')

@main.route('/about', methods=['GET'])
def about_page():
    return render_template('about.html')

@main.route("/classes", methods=["GET"])
def classes_page():
    return render_template("classes.html")

@main.route('/api/status', methods=['GET'])
def index():
    return jsonify({"status": "berhasil",
                    "message": "API Klasifikasi Tumor Otak berjalan"})
    
@main.route('/api/predict', methods=['POST'])
def predict_route():
    if "img" not in request.files:
        return jsonify({"status": "gagal",
                        "message": "Tidak ada file yang diunggah"}), 400
    file = request.files['img']
    if file.filename == '':
        return jsonify({"status": "gagal",
                        "message": "Nama file tidak valid"}), 400
    if not allowed_file(file.filename):
        return jsonify({"status": "gagal",
                        "message": "Format file tidak didukung, Upload file dengan format JPG, JPEG, atau PNG"}), 400

    filename = secure_filename(file.filename)
    upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(upload_path)
    
    try:
        result = predict(upload_path)
        return jsonify({"status": "berhasil",
                        "filename": filename,
                        "predicted": result["predicted_class"],
                        "confidence": result["confidence"],
                        "all_probabilities": result["all_probabilities"],
                        }), 200
    except Exception as error:
        return jsonify({"status": "gagal",
                        "message": f"Terjadi kesalahan saat memproses gambar: {str(error)}"}), 500
