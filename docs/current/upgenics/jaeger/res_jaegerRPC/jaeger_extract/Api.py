from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
import requests
import json

import registrator

from JaegerExtractAPI import TestExtract

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Connection to models
TestExtract_Provider = TestExtract()

# Distributed Tracing
import jaegerTracing
tracer = jaegerTracing.getTracerInstance()
from flask_opentracing import FlaskTracing
tracing = FlaskTracing(tracer, True, app)


@app.route('/extract', methods=['GET'])
def testjaegerExtract():
    try:
        application_status = TestExtract_Provider.extractSpan()
        return "server1"
    except Exception as ex:
        return jsonify(str(ex)), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')
