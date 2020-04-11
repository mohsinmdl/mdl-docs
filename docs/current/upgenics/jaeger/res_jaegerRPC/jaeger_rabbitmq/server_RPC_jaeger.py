def callback(self, ch, method, properties, body):
        span_ctx = tracer.extract(format=Format.TEXT_MAP, carrier=properties.headers)
        with tracer.start_active_span('callback', child_of=span_ctx) as scope:
            data = json.loads(str(body.decode("utf-8")))
            print("RECEIVED DATA: " , data)
            innerData = data['data']
            if 'userImage' in innerData.keys():
                print("FIRST")
                insert_query = "INSERT INTO UserPersonalInfos (userId, legalName, image) VALUES (%s, %s, %s)"
                insert_data = (data['user_id'], data['data']['userName'], data['data']['userImage'])
                
            else :
                print("SECOND")
                insert_query = "INSERT INTO UserPersonalInfos (userId, legalName) VALUES (%s, %s)"
                insert_data = (data['user_id'], data['data']['userName'])
            
            cursor = self.mysqlConnection.cursor()
            scope.span.set_tag("query", insert_query)
            scope.span.set_tag("queryData", insert_data)
            cursor.execute(insert_query, insert_data)
            self.mysqlConnection.commit()
            print("Personal Information Inserted Successfully.")