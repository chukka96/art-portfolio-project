import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# ---------------- CONFIG ----------------
UPLOAD_BASE = "static/uploads"

ALLOWED_EXTENSIONS = {
    "posters": {"jpg", "jpeg", "png"},
    "certifications": {"pdf"},
    "edits": {"mp4"}
}

# Ensure folders exist
for folder in ALLOWED_EXTENSIONS.keys():
    os.makedirs(os.path.join(UPLOAD_BASE, folder), exist_ok=True)

# ---------------- HELPERS ----------------
def get_category(filename):
    if "." not in filename:
        return None
    ext = filename.rsplit(".", 1)[1].lower()
    for category, exts in ALLOWED_EXTENSIONS.items():
        if ext in exts:
            return category
    return None

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    gallery_data = {}

    for category in ALLOWED_EXTENSIONS.keys():
        folder_path = os.path.join(UPLOAD_BASE, category)
        files = os.listdir(folder_path) if os.path.exists(folder_path) else []
        gallery_data[category.capitalize()] = files

    return render_template("gallery.html", gallery_data=gallery_data)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            return "No file selected", 400

        filename = secure_filename(file.filename)
        category = get_category(filename)

        if not category:
            return "Unsupported file type", 400

        save_path = os.path.join(UPLOAD_BASE, category, filename)
        file.save(save_path)

        return redirect(url_for("gallery"))

    return render_template("upload.html")

if __name__ == "__main__":
    app.run()
