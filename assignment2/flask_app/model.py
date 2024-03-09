from sqlalchemy.exc import IntegrityError
from flask_app import db


class EntityToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity = db.Column(db.String(80))
    token = db.Column(db.String(40))
    head = db.Column(db.String(80))
    relation = db.Column(db.String(20))

    def __repr__(self):
        return f"EntityToken('{self.entity}', '{self.token}', '{self.head}', '{self.relation}')"

    @classmethod
    def add(cls, entity: str, token: str, head: str, relation: str) -> str | IntegrityError:
        try:
            ent_tok = EntityToken(entity=entity, token=token, head=head, relation=relation)
            db.session.add(ent_tok)
            db.session.commit()
            return str(ent_tok)
        except IntegrityError as e:
            db.session.rollback()
            return e

    @classmethod
    def add_all(cls, entities: list[tuple], dependencies: dict[int, tuple]) -> None:
        for entity in entities:
            entity_text = entity[3]
            tokens = entity_text.split()
            for i, token in enumerate(tokens):
                # match token to dependency
                token_id = entity[4] + i
                dependency = dependencies[token_id]
                head = dependency[2]
                dep = dependency[1]
                # add to database
                cls.add(entity_text, token, head, dep)
