import os, tensorflow as tf
from preprocessing import preprocess_image

def predict_currency(model_path, img_path, class_names):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}. Train and save a model first.")
    model = tf.keras.models.load_model(model_path)
    img = preprocess_image(img_path)
    img = img.reshape(1,224,224,1)
    pred = model.predict(img)
    return class_names[pred.argmax()]
