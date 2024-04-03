# Assignment 3: Runtime Instructions
From the assignment3 directory, run
```bash
$ docker-compose up
```

## FastAPI
In a new terminal window, get the container ID using `docker ps`, then run one of the following commands. The first gets the API description and usage. The second posts
the input's named entities. The last posts the input's dependencies.
```bash
$ docker exec -i <ID> curl http://127.0.0.1:8000/
$ docker exec -i <ID> curl http://127.0.0.1:8000/ner -H "Content-Type: application/json" -d@app_fastapi/input.json
$ docker exec -i <ID> curl http://127.0.0.1:8000/dep -H "Content-Type: application/json" -d@app_fastapi/input.json
```
Any of the commands optionally accepts a "pretty" parameter, which neatens the API output when true. Usage looks like:
```bash
$ docker exec -i <ID> curl http://127.0.0.1:8000?pretty=true
```

## Flask
Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the Flask application.

## Streamlit
Navigate to [http://127.0.0.1:8501](http://127.0.0.1:8501) to view the Streamlit application.
