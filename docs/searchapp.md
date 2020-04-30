# Search App with React & Elasticsearch
***

## Aim

The aim of this documentation is to provide  working knowledge of the following technologies.

- Neo4j
- Elasticsearch
- Kibana
- React

## What you will need?

- Elasticsearch Docker container
- Neo4j Docker container
- Internet Connection for React.js CDN

## Outline

This documentation divided into two parts:


- Firstly - **Synchronization** of Neo4j data with Elasticsearch
- Lastly - **Searching** data from Elasticsearch using React


## Synchronization of Neo4j data with Elasticsearch



**Step 01 - Initializing Neo4j Container**

You can initialize a docker container through docker-compose file with the following snippet.

> docker-compose.yml

```bash
version: "3"
services:

  neo4j:
    image: neo4j:3.5.6
    networks:
       kong-net:
          aliases:
          - neo4j
    ports:
      - "7474:7474"
      - "7473:7473"
      - "7687:7687"
    working_dir: /var/lib/neo4j/data
    volumes:
      - $HOME/neo4j/conf:/var/lib/neo4j/conf
      - $HOME/neo4j/data:/var/lib/neo4j/data
      - $HOME/neo4j/logs:/var/lib/neo4j/logs
      - $HOME/neo4j/import:/var/lib/neo4j/import
      - $HOME/neo4j/plugins:/var/lib/neo4j/plugins
    deploy:
      replicas: 1

networks:
  kong-net:
    external: true
volumes:
  neo4j-data:
  neo4j-conf:
  neo4j-plugins:
```
!!! note
    you can find `docker-compose.yml` file in the attached `helping-scripts` folder.



**Step 02 - Download Plugins**



Download the jar from the [latest release.](https://github.com/neo4j-contrib/neo4j-elasticsearch/releases)


and put the jar file to $NEO4J_HOME/plugins folder.


**Step 03 - Modify `neo4j.conf `**


Modify $NEO4J_HOME/conf/neo4j.conf accordingly (see the snippet below)


```
elasticsearch.host_name=http://elasticsearch:9200
elasticsearch.index_spec=neo-person:Person(name,born), neo-movie:Movie(title,tagline,released)
```

With that in place, the above snippet track changes of `Person` and `Movie` node from the neo4j database to the Elasticsaerch instance running on `elasticsearch:9200`.


!!! hint ""
    To perform an initial import, you can run the movie example from neo4j


**Step 04 - Running an Elasticsearch container**

You can initialize a docker container through docker-compose file with the following snippet.

> docker-compose.yml

```bash
version: '2'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:6.0.0
    restart: always
    container_name: elasticsearch
    hostname: elasticsearch
    networks:
      kong-net:
          aliases:
          - elasticsearch
    environment:
      - bootstrap.memory_lock=true
      - ES_JAVA_OPTS=-Xms512m -Xmx512m
    ports:
      - "9200:9200"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    mem_limit: 1g
    volumes:
      - esdata1:/usr/share/elasticsearch/data
      - eslog:/usr/share/elasticsearch/logs
      - ./config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml
  kibana:
    image: docker.elastic.co/kibana/kibana:6.0.0
    container_name: kibana
    ports:
      - "5601:5601"
    environment:
      ELASTICSEARCH_URL: http://elasticsearch:9200
    depends_on:
    - elasticsearch
    networks:
      kong-net:
          aliases:
          - kibana

volumes:
  esdata1:
    driver: local
  eslog:
    driver: local
    
networks:
  kong-net:
    external: true
```

!!! note
    you can find `docker-compose.yml` file in the attached `helping-scripts` folder.


**Step 05 - Append the following snippet to elasticsaerch.yml file**


```
# CORS

http.cors.enabled : true
http.cors.allow-origin : "*"
http.cors.allow-methods : OPTIONS, HEAD, GET, POST, PUT, DELETE
http.cors.allow-headers : "X-Requested-With,X-Auth-Token,Content-Type, Content-Length, Authorization"
http.cors.allow-credentials: true
```
!!! note
    you can find `elasticsearch.yml` file in the attached `helping-scripts`.



## Searching data from Elasticsearch using React

This react app provide you an interface to search the data from the elasticsearch.

> index.html

```html
<!DOCTYPE html>
<html>

<head>
    <title>React Project</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
        integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <script src="https://unpkg.com/react@16.7.0/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@16.7.0/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <style>
        .heading {
            color: purple;
        }
    </style>

</head>

<body>
    <div id="root"></div>
    <script type="text/babel">


        const Movies = ({ movies }) => {
            console.log("RESULT : " , movies)
            return (
                <div>
                    <div className="card">
                        <div className="card-body">
                            <h1 className="card-title">Title: {movies.title}</h1>
                            <p className="card-text">id: {movies.id}</p>
                            <p className="card-subtitle mb-2 text-muted">released: {movies.released}</p>
                            <p className="card-text">tagline: {movies.tagline}</p>
                        </div>
                    </div>
                </div>
            )
        };

        const MoviesList = ({ movies }) => {
            return (
                <div>
                    {console.log("Going to iterate list from MoviesList")}
                    {movies.map((item, i) => (
                        <Movies movies={item} />
                    ))}
                </div>
            )
        };

 
        class InputApp extends React.Component {


            constructor(props) {
                super(props);

                this.state = {
                    moviesCollectin: false,
                    username: '',
                    movieName: '',
                    movies: [],
                    moviesData: [],
                }

                this.updateInput = this.updateInput.bind(this);
                this.handleSubmit = this.handleSubmit.bind(this);
                this.updateInputName = this.updateInputName.bind(this);
                this.searchViaName = this.searchViaName.bind(this);

            }


            updateInput(event) {
                this.setState({ username: event.target.value })
            }

            updateInputName(event) {
                this.setState({ movieName: event.target.value })
            }


            handleSubmit() {

                this.setState({ moviesCollectin: false })
                console.log('Your input value is: ' + '"' + this.state.username + '"');
                fetch('http://localhost:9200/neo-movie/Movie/' + this.state.username)
                    .then(res => res.json())
                    .then((data) => {
                        this.setState({ movies: data._source })
                        console.log(data._source)
                    })
                    .catch(console.log)
                //Send state to the server code
            }

            searchViaName() {


                console.log('Your input value is: ' + this.state.movieName);
                fetch('http://localhost:9200/*/_search?q=title:' + this.state.movieName)
                    .then(res => res.json())
                    .then((data) => {

                        console.log(data.hits.hits)
                        let allmovies = data.hits.hits;
                        let tempMovies = [];
                        allmovies.forEach(elem => {
                            tempMovies.push({

                                id: elem['_source'].id,
                                labels: elem['_source'].labels,
                                tagline: elem['_source'].tagline,
                                title: elem['_source'].title,
                                released: elem['_source'].released

                            });
                        });
                        // console.log("before tempMovies " + typeof(tempMovies))
                        this.setState({ moviesData: tempMovies })
                        console.log("Going to iterate list")
                        this.state.moviesData.map(function (item, i) {
                            console.log(item)
                        })
                        // console.log("moviesdata"+ this.state.moviesData + "typeof" + typeof(this.state.moviesData)) 
                        this.setState({ moviesCollectin: true })
                    })
                    .catch(console.log)
                //Send state to the server code


            }



            render() {
                return (

                    <div>

                        <div className="jumbotron"><center><h1>Elasticsearch-React Search Demo Search App</h1></center></div>
                        <div className="container">
                            <div className='input-group'>
                                <input type="text" className="form-control" onChange={this.updateInput} placeholder="Search by ID"></input>
                                <input type="submit" onClick={this.handleSubmit} ></input>

                                <input type="text" className="form-control" onChange={this.updateInputName} placeholder="Search by Title"></input>
                                <input type="submit" onClick={this.searchViaName} ></input>
                            </div>

                            {console.log("Going to iterate list from render()")}
                            {this.state.moviesData.map(function (item, i) {
                                console.log(item)
                            })}


                            {this.state.moviesCollectin
                                ? <MoviesList movies={this.state.moviesData} />
                                : <Movies movies={this.state.movies} />}

                        </div>
                    </div>


                );
            }
        }


        ReactDOM.render(
            <InputApp />,
            document.getElementById("root")
        );
    </script>

</body>

</html>
```


!!! note
    you can find `index.html` file in the attached `helping-scripts` folder.


## Conclusion
This documentation presents a working example of making a simple search app for elasticsearch data.

Hope it helps, please let me know if you have any questions or feedback. I might miss something, I need to hear from you. JazakAllahu khaira :)