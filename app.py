from flask import Flask, render_template, request, make_response, jsonify, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os

import logic

ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploaded_files"

@app.route("/")
def home():
    return render_template("index.html")

def allowed_extension(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.errorhandler(413)
def too_large(e):
    return make_response(jsonify(message="File is too large!"), 413)

@app.route("/upload", methods=["POST"])
def upload_file():
    if request.method == "POST":
        files = request.files.getlist('files')
        for file in files:
            print(file)
            if allowed_extension(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        logic.main()
        return redirect(url_for("home"))
        
    return "No file Uploaded!", 400

@app.route("/download")
def download_file():
    output_file = os.path.abspath("output.xls")
    return send_file(output_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
