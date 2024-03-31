from flask import request, render_template
import ner
from flask_app import app
from flask_app.model import EntityToken


@app.route('/')
def index_get():
    return render_template('form.html', input=open('input.txt').read())


@app.post('/results')
def index_post():
    # process
    text = request.form['text']
    doc = ner.SpacyDocument(text)
    markup = doc.get_entities_with_markup()

    # format
    markup_paragraphed = ''
    for line in markup.split('\n'):
        if line.strip() == '':
            markup_paragraphed += '<p/>\n'
        else:
            markup_paragraphed += line

    # add to database
    EntityToken.add_all(doc.get_entities(), doc.get_parse())

    return render_template('spacy.html', markup=markup_paragraphed, dep_graph=doc.get_parse_graph(),
                           dep_table=doc.get_parse_table())


@app.get('/database')
def get_db():
    return render_template('database.html', db=EntityToken.query.all())
