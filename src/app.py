import os.path

from flask import Flask, redirect, render_template, request
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    check_directory()
    for file in request.files.getlist("file"):
        filename = secure_filename(file.filename)
        file.save(os.path.join("photos", filename))
        return redirect("/")
    
def check_directory():
    if not os.path.exists("photos"):
        os.makedirs("photos")

def main():
    check_directory()
    app.run(host="0.0.0.0", port=8388)

if __name__ == "__main__":
    main()