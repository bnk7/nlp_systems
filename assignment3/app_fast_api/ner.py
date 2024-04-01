import io
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")


class SpacyDocument:

    def __init__(self, text: str):
        self.text = text
        self.doc = nlp(text)

    def get_tokens(self) -> list[str]:
        return [token.lemma_ for token in self.doc]

    def get_entities(self) -> list[tuple]:
        entities = []
        for e in self.doc.ents:
            entities.append((e.start_char, e.end_char, e.label_, e.text, e.start))
        return entities

    def get_entities_with_markup(self) -> str:
        entities = self.doc.ents
        starts = {e.start_char: e.label_ for e in entities}
        ends = {e.end_char for e in entities}
        buffer = io.StringIO()
        for i, char in enumerate(self.text):
            if i in ends:
                buffer.write('</entity>')
            if i in starts:
                buffer.write('<entity class="%s">' % starts[i])
            buffer.write(char)
        markup = buffer.getvalue()
        return '<markup>%s</markup>' % markup

    def get_parse(self, sentence=None) -> dict[int, tuple]:
        # use the entire doc if no sentence is passed
        document = sentence if sentence else self.doc
        parse = {token.i: (token.text, token.dep_, token.head.text) for token in document}
        return parse

    def get_parse_per_sent(self) -> list[dict[int, tuple]]:
        return [self.get_parse(sent) for sent in self.doc.sents]

    def get_parse_table(self) -> str:
        table = '<table><tr><th>Token</th><th>Dependency</th><th>Head</th></tr>'
        for token in self.doc:
            row = '<tr><td>' + token.text + '</td><td>' + token.dep_ + '</td><td>' + token.head.text + '</td></tr>'
            table += row
        return table + '</table>'

    def get_parse_graph(self) -> str:
        graph = ''
        for sent in self.doc.sents:
            graph += displacy.render(sent, style='dep', options={'compact': True, 'distance': 100})
        return graph


if __name__ == '__main__':

    example = (
        "My name is Percy Jackson. "
        "I'm twelve years old. Until a few months ago, I was a boarding student at Yancy Academy, "
        "a private school for troubled kids in upstate New York. "
        "Am I a troubled kid? "
        "Yeah. You could say that.")

    doc = SpacyDocument(example)
    print(doc.get_tokens())
    for entity in doc.get_entities():
        print(entity)
    print(doc.get_entities_with_markup())
    print(doc.get_parse_per_sent())
    print(doc.get_parse_graph())
    print(doc.get_parse_table())
