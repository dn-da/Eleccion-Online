from app import db
from app import ma

class Propuesta(db.Model):
    __tablename__ = 'propuesta'
    id_propuesta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(255), nullable=True)
    id_lista = db.Column(db.Integer, db.ForeignKey('lista_candidato.id_lista'), nullable=True)
    
    def __init__(self, descripcion, id_lista):
        self.descripcion = descripcion
        self.id_lista = id_lista


class PropuestaSchema(ma.Schema):
    class Meta:
        fields = (
            'id_propuesta',
            'descripcion',
            'id_lista_candidato'
        )

