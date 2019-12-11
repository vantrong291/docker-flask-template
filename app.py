import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


@app.route('/', methods=['POST', 'GET'])
def mainHandler():
    return "main handler"


# app.run()
app.run(debug=True, host='0.0.0.0')
