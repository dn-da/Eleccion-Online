import enum

from sqlalchemy import Enum

from app import db
from app.models.Propuesta import Propuesta
from app.models.Candidato import Candidato

class EstadoListaEnum(enum.Enum):
    aprobado = "aprobado"
    desaprobado = "desaprobado"
    pendiente = "pendiente"


class ListaCandidato(db.Model):
    __tablename__ = 'lista_candidato'
    id_lista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=True)
    estado = db.Column(Enum(EstadoListaEnum), nullable=True, default=EstadoListaEnum.pendiente)
    id_eleccion = db.Column(db.Integer, db.ForeignKey('eleccion.id_eleccion'), nullable=True)

    propuestas = db.relationship('Propuesta', backref='listacandidato', lazy=True)
    
    candidatos = db.relationship('Candidato', backref='listacandidato', lazy=True)

    def __init__(self, nombre, id_eleccion, estado=EstadoListaEnum.pendiente):
        self.nombre = nombre
        self.id_eleccion = id_eleccion
        self.estado = estado