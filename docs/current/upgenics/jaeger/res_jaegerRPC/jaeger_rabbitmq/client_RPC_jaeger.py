def save_user_created(self, user_id, content):
        try:
            with tracer.start_active_span('save_user_created') as scope:
                scope.span.set_tag('args', [user_id, content])

                # Distributed Tracing (Injecting Span)
                span = get_current_span()
                carrier = {}
                tracer.inject(span_context=span.context, format=Format.TEXT_MAP, carrier=carrier)
                
                _now = str(datetime.now())
                # publish notification for job applied
                message = {"user_id": user_id, "dated": _now, "data": content}
                message_str = json.dumps(message)
                print("sending body to save : " + message_str)
                # RabbitMQ Connection
                connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
                # connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
                channel = connection.channel()
                channel.basic_publish(
                    exchange='save_user_name_image',
                    routing_key='',
                    body=message_str,
                    properties=pika.BasicProperties(headers=carrier)
                    )
                connection.close()
                span.finish()
                # Return REST Reply
                return jsonify({"message": "User Name and Image Saved Mysql"}), 201
        except Exception as ex:
            scope.span.set_tag('Exception', ex)
            return jsonify(str(ex)), 500
        






        