from flask import Flask
from flask import request
from inferor import Inferor

inferor = Inferor()
app = Flask(__name__)

@app.route("/", methods=["POST"])
def hello():
    if not request.files or not request.files["image"]:
        return "No File Uploaded"
    image = request.files["image"]
    return "barev::::: " + str(inferor.infer(image))

if __name__ == "__main__":
    app.run()