import os
from uuid import uuid4
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from font_recognition import predict_font  # your function

# On Render the repo is checked out to /opt/render/project/src
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_UPLOAD_DIR = os.path.join(PROJECT_ROOT, "static", "uploads")

app = Flask(__name__)

# Render’s filesystem is ephemeral across deploys, but writable at runtime.
# Using the app folder is fine for small temp uploads; for permanence, use S3, etc.
app.config["UPLOAD_FOLDER"] = os.environ.get("UPLOAD_FOLDER", DEFAULT_UPLOAD_DIR)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            return redirect(request.url)

        if allowed_file(file.filename):
            # avoid name collisions
            original = secure_filename(file.filename)
            ext = original.rsplit(".", 1)[1].lower()
            filename = f"{uuid4().hex}.{ext}"
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            prediction = predict_font(filepath)

            return render_template(
                "index.html",
                prediction=prediction,
                uploaded_image=filename,
            )
        return redirect(request.url)

    return render_template("index.html")

if __name__ == "__main__":
    # On Render you must bind 0.0.0.0 and use the provided PORT env var
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("FLASK_DEBUG") == "1")