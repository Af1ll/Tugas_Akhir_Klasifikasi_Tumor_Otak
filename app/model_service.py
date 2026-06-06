import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

model_path = "D:\\Tugas Akhir\\Sistem Klasifikasi Tumor Otak\\models\\InceptionV3_brain_tumor_Eks2.keras"
model = load_model(model_path)

class_names = ['glioma',
                'meningioma',
                'no_tumor',
                'pituitary']

def preprocess_image(image_path):
    img = Image.open(image_path).convert('RGB')
    img = img.resize((299, 299))
    img_array = np.array(img).astype("float32")
    # img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict(image_path):
    preprocessed_image = preprocess_image(image_path)
    predictions = model.predict(preprocessed_image)
    probability = predictions[0]
    
    predicted_index = int(np.argmax(probability))
    predicted_class = class_names[predicted_index]
    confidence = float(probability[predicted_index])
    
    all_probabilities = {}
    
    for i, class_name in enumerate(class_names):
        all_probabilities[class_name] = float(probability[i])
        
    return {
        "predicted_class": predicted_class,
        "confidence": confidence,
        "all_probabilities": all_probabilities
    }