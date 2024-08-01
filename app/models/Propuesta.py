from app import db
from app import ma

class Propuesta(db.Model):
    __tablename__ = 'propuesta'
    id_propuesta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(255), nullable=True)
    denegada = db.Column(db.Boolean, nullable=True, default=False)
    id_lista = db.Column(db.Integer, db.ForeignKey('lista_candidato.id_lista'), nullable=True)

    lista_candidato = db.relationship('ListaCandidato', backref='propuestasl', lazy=True)

    def __init__(self, descripcion, id_lista, denegada=False):
        self.descripcion = descripcion
        self.id_lista = id_lista
        self.denegada = denegada

class PropuestaSchema(ma.Schema):
    class Meta:
        fields = (
            'id_propuesta',
            'descripcion',
            'denegada',
            'id_lista'
        )

