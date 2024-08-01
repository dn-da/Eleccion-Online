from app import db
from app import ma

class Voto(db.Model):
    __tablename__ = 'voto'
    id_voto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_elector = db.Column(db.Integer, db.ForeignKey('elector.id'), nullable=True)
    id_lista = db.Column(db.Integer, db.ForeignKey('lista_candidato.id_lista'), nullable=True)

    def __init__(self, id_elector, id_lista):
        self.id_elector = id_elector
        self.id_lista = id_lista

class VotoSchema(ma.Schema):
    class Meta:
        fields = (
            'id_voto',
            'id_elector',
            'id_lista'
        )