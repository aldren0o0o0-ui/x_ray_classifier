# Pnuenomia

A Flask web app for classifying chest X-ray images into:

- `COVID19`
- `NORMAL`
- `PNEUMONIA`

The app uses a trained TensorFlow/Keras model and a simple upload interface.

## Project structure

```text
pnuenomia/
|-- app.py
|-- requirements.txt
|-- model/
|   |-- covid_pneumonia_classifier_final.keras
|   `-- covid_pneumonia_classifier_labels.json
|-- static/
|   |-- style.css
|   `-- uploads/
`-- templates/
    `-- index.html
```

## Run locally

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Start the app:

```powershell
python app.py
```

4. Open `http://127.0.0.1:5000`

## Notes

- Uploaded images are stored in `static/uploads/` and are ignored by Git.
- The model file is included in this project. GitHub allows files up to 100 MB, and this model is within that limit.
- This project is for educational use and not for medical diagnosis.

## Push to GitHub

Run these commands inside the `pnuenomia` folder after creating an empty GitHub repository:

```powershell
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```
