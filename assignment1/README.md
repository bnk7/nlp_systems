# Assignment 1: Runtime Instructions
I ran the code on Python 3.10. The necessary packages are listed in requirements.txt.

## FastAPI
In the terminal, run the following line to start the API:
```bash
$ uvicorn app_fastapi:app --reload
```
In another window, run one of the following commands. The first gets the API description and usage. The second posts
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
Run the following line in the terminal, and then navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) or 
[http://127.0.0.1:5000/get](http://127.0.0.1:5000/get) in the browser.
```bash
$ python app_flask.py
```

## Streamlit
Running this command will open a window in your browser and start the service:
```bash
$ python -m streamlit run app_streamlit.py
```