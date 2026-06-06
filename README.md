# Brain Tumor Classification API

Sistem RESTful API untuk klasifikasi tumor otak berbasis Flask.

## Deskripsi

Project ini merupakan implementasi model klasifikasi tumor otak ke dalam sistem RESTful API menggunakan Flask. API menerima input berupa citra MRI otak, kemudian melakukan preprocessing dan prediksi menggunakan model deep learning yang telah dilatih sebelumnya.

## Teknologi yang Digunakan

- Python
- Flask
- TensorFlow / Keras
- Pillow
- NumPy
- Pipenv

## Struktur Project

```text
brain-tumor-api/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── model_service.py
│   └── utils.py
├── models/
├── uploads/
├── run.py
├── Pipfile
├── Pipfile.lock
└── README.md


**Cara Menjalankan Projek**

Install dependency:
pipenv install

Masuk ke virtual environment:
pipenv shell

Jalankan server:
python run.py

Server berjalan pada:
http://127.0.0.1:5000

**Endpoint API**
*Cek Status API*
GET /

*Prediksi Tumor Otak*
POST /api/predict

Body menggunakan form-data:
| Key   | Type |
| ----- | ---- |
|  img  | File |

Contoh response:
{
  "status": "success",
  "prediction": "glioma",
  "confidence": 0.95
}

**Catatan**

File model tidak disertakan di repository ini. Letakkan file model pada folder models/ sebelum menjalankan sistem.

