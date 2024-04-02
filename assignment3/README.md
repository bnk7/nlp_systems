# Assignment 3: Runtime Instructions
## Fastapi
```
cd app_fastapi
docker build -t assignment3_fastapi .
docker run -dp 8000:8000 assignment3_fastapi
```
Run one of the following commands. The first gets the API description and usage. The second posts
the input's named entities. The last posts the input's dependencies.
```bash
$ curl http://127.0.0.1:8000/
$ curl http://127.0.0.1:8000/ner -H "Content-Type: application/json" -d@input.json
$ curl http://127.0.0.1:8000/dep -H "Content-Type: application/json" -d@input.json
```
Any of the commands optionally accepts a "pretty" parameter, which neatens the API output when true. Usage looks like:
```bash
$ curl http://127.0.0.1:8000?pretty=true
```
## Flask
```
cd app_flask
docker build -t assignment3_flask .
docker run -dp 5000:5000 assignment3_flask
```
Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)
## Streamlit
```
cd app_streamlit
docker build -t assignment3_streamlit .
docker run -dp 8501:8501 assignment3_streamlit
```
Go to [http://127.0.0.1:8501](http://127.0.0.1:8501)