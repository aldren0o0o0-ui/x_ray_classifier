import os
import json
import numpy as np
import tensorflow as tf

from flask import Flask, render_template, request, url_for
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
MODEL_PATH = os.path.join(BASE_DIR, "model", "covid_pneumonia_classifier_final.keras")
LABELS_PATH = os.path.join(BASE_DIR, "model", "covid_pneumonia_classifier_labels.json")

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = tf.keras.models.load_model(MODEL_PATH)

with open(LABELS_PATH, "r") as f:
    class_names = json.load(f)

IMG_SIZE = (224, 224)  # Change to (160, 160) if you trained using 160x160


def predict_image(img_path):
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # Use this only if your model does NOT already include preprocess_input layer
    # If your training code already has preprocess_input inside the model, remove this line.
    # img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_index]
    confidence = float(predictions[0][predicted_index]) * 100

    scores = {
        class_names[i]: round(float(predictions[0][i]) * 100, 2)
        for i in range(len(class_names))
    }

    return predicted_class, round(confidence, 2), scores


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    scores = None
    image_url = None

    if request.method == "POST":
        file = request.files.get("image")

        if file and file.filename != "":
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            prediction, confidence, scores = predict_image(filepath)
            image_url = url_for("static", filename=f"uploads/{filename}")

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        scores=scores,
        image_url=image_url
    )


if __name__ == "__main__":
    app.run(debug=True)
