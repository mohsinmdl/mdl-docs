import pymongo
from datetime import datetime
import pika
import json
from flask import jsonify
from bson.objectid import ObjectId


# Distributed Tracing
from opentracing_instrumentation.request_context import get_current_span, span_in_context
import jaegerTracing
tracer = jaegerTracing.getTracerInstance()
from opentracing.propagation import Format



class TestExtract():
    

    def extractSpan(self):
        span_ctx = tracer.extract(format=Format.TEXT_MAP, carrier={})
        with tracer.start_active_span(operation_name='extractSpan', child_of=span_ctx) as scope:
            scope.span.set_tag('args', 'input values here')

        return "Server2"