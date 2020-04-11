from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
import requests
import json

import registrator

from JaegerInjectAPI import TestInject

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Connection to models
JaegerInjectAPI_Provider = TestInject()

# Distributed Tracing
import jaegerTracing
tracer = jaegerTracing.getTracerInstance()
from flask_opentracing import FlaskTracing
tracing = FlaskTracing(tracer, True, app)


@app.route('/inject', methods=['GET'])
def testjaegerInject():
    try:
        application_status = JaegerInjectAPI_Provider.injectSpan()
        return str(application_status)
    except Exception as ex:
        return jsonify(str(ex)), 500





if __name__ == '__main__':
    app.run(host='0.0.0.0')
