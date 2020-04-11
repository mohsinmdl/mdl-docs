# HTTP and RPC calls with Jaegers


## HTTP Calls
***


### Client Files

``` python tab="API.py"

{!current/upgenics/jaeger/res_jaegerRPC/jaeger_inject/Api.py!}

```

``` python tab="JaegerInjectAPI.py"

{!current/upgenics/jaeger/res_jaegerRPC/jaeger_inject/JaegerInjectAPI.py!}

```


### Server Files

``` python tab="API.py"

{!current/upgenics/jaeger/res_jaegerRPC/jaeger_extract/Api.py!}

```

``` python tab="JaegerExtactAPI.py"

{!current/upgenics/jaeger/res_jaegerRPC/jaeger_extract/JaegerExtractAPI.py!}

```


### Useful Code Snippets
***

#### Client side
```python
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
```


#### Server side

```python
def extractSpan(self):
        span_ctx = tracer.extract(format=Format.TEXT_MAP, carrier={})
        with tracer.start_active_span(operation_name='extractSpan', child_of=span_ctx) as scope:
            scope.span.set_tag('args', 'input values here')

        return "Server2"
```


## RPC via RabbitMQ

### Client Call
``` python tab="client_RPC_jaeger.py"

{!current/upgenics/jaeger/res_jaegerRPC/jaeger_rabbitmq/client_RPC_jaeger.py!}

```


### Exchange-Consumer Call
``` python tab="client_RPC_jaeger.py"

{!current/upgenics/jaeger/res_jaegerRPC/jaeger_rabbitmq/server_RPC_jaeger.py!}

```