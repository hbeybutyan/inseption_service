from flask import Flask
from flask import request
from flask import jsonify
from inferor import Inferor

inferor = Inferor()
app = Flask(__name__)

@app.route("/", methods=["POST"])
def hello():
    if not request.files or not request.files["image"]:
        return response_with_400("Bad request type. Missing image in payload.")
    image = request.files["image"].read()
    return jsonify(inferor.infer(image))


@app.errorhandler(400)
def error_handler(error):
    app.logger.info("Possible problem is wrong request type.")
    return response_with_400("Possible problem is wrong request type.")


@app.errorhandler(404)
def error_handler(error):
    app.logger.info("Requested resource does not exist.")
    resp = jsonify({"error_message": "Requested resource does not exist."})
    resp.status_code = 404
    return resp


@app.errorhandler(500)
def error_handler(error):
    return response_with_500()


@app.errorhandler(Exception)
def error_handler(exception):
    return response_with_500()


def response_with_400(errorMessage):
    app.logger.info(errorMessage)
    resp = jsonify(({"error_message": errorMessage}))
    resp.status_code = 400
    return resp


def response_with_500():
    app.logger.info("Internal server error.")
    resp = jsonify(({"error_message": "Internal server error."}))
    resp.status_code = 500
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
