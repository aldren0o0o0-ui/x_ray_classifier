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


1. PrerequisitesMake sure you have Git installed on your machine. You can verify this by running:bash
```powershell
git --version
```
2. Clone the RepositoryOn GitHub.com, navigate to the main page of the repository.Above the list of files, click the green Code button.Copy the URL for the repository (HTTPS is recommended for beginners):

https://github.comOpen your terminal (or Command Prompt).Change the current working directory to the location where you want the cloned directory.Type git clone, and then paste the URL you copied earlier:bashgit clone https://github.com
```powershell
git clone https://github.com/aldren0o0o0-ui/x_ray_classifier.git
```
Press Enter to create your local clone.
3. Navigate to the ProjectMove into the project directory to start working
```powershell
 cd x_ray_classifier
```
## Push to GitHub

Run these commands inside the `pnuenomia` folder after creating an empty GitHub repository:

```powershell
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/aldren0o0o0-ui/x_ray_classifier.git
git push -u origin main
```
