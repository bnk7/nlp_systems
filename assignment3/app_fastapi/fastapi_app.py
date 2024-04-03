"""
FastAPI interface to spaCy NER and dependency parsing

$ curl http:/127.0.0.1:8000
$ curl -X POST -H 'accept: application/json' -H 'Content-Type: application/json' -d@input.json http:/127.0.0.1:8000

"""

import json
from fastapi import FastAPI, Response
from pydantic import BaseModel
from app_fastapi.ner import SpacyDocument

app = FastAPI()


class Item(BaseModel):
    text: str = ''


@app.get('/')
def index(pretty: bool = False):
    content = "Content-Type: application/json"
    url = "http://127.0.0.1:8000/"
    answer = {
        "description": "Interface to the spaCy entity extractor and dependency parser",
        "entity extractor usage": 'curl %sner -H "%s" -d@input.json' % (url, content),
        "dependency parser usage": 'curl %sdep -H "%s" -d@input.json' % (url, content)}
    if pretty:
        answer = prettify(answer)
    return answer


@app.post('/ner')
def ner_process(item: Item, pretty: bool = False):
    doc = SpacyDocument(item.text)
    answer = {"input": item.text, "output": doc.get_entities()}
    if pretty:
        answer = prettify(answer)
    return answer


@app.post('/dep')
def ner_index(item: Item, pretty: bool = False):
    doc = SpacyDocument(item.text)
    answer = {"input": item.text, "output": doc.get_parse()}
    if pretty:
        answer = prettify(answer)
    return answer


def prettify(result: dict):
    json_str = json.dumps(result, indent=2)
    return Response(content=json_str, media_type='application/json')
