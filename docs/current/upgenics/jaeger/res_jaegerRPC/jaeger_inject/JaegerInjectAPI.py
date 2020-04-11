
import json
from flask import jsonify
import requests

# Distributed Tracing
from opentracing_instrumentation.request_context import get_current_span, span_in_context
import jaegerTracing
tracer = jaegerTracing.getTracerInstance()
from opentracing.propagation import Format

 
class TestInject():
  
    def injectSpan(self):
        with tracer.start_active_span('injectSpan') as scope:
            scope.span.set_tag("args", "I hope you will see me in server side")
            
            # Distributed Tracing with Jaeger
            carrier = {"Content-Type": "application/json"}
            tracer.inject(
                span_context=scope.span.context,
                format=Format.TEXT_MAP,
                carrier=carrier)
            
            url = 'http://jaegerextract:5000/extract'
            # url = 'http://localhost:6570/company/searchByName'
            data = json.dumps({'keyword':"Mohsin"})
            response = requests.get(url, data = data, headers = carrier)
            return response


