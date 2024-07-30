import logging

from app import db
from app.models.Eleccion import Eleccion
from app.models.Eleccion import EleccionSchema
from app.models.Candidato import Candidato
from app.models.Candidato import CandidatoSchema
from app.models.ListaCandidato import ListaCandidato
from app.models.Elector import Elector
from app.models.Voto import Voto
from app.models.Propuesta import PropuestaSchema
from app.services.IEleccionServicio import IEleccionServicio
from app.services.IEleccionServicio import IListaServicio
from app.services.IEleccionServicio import ICandidatoServicio

logger = logging.getLogger(__name__)

eleccion_schema = EleccionSchema()
eleccion_schemas = EleccionSchema(many = True)
candidato_schema = CandidatoSchema()
propuesta_schema = PropuestaSchema()

class EleccionServicioImpl(IEleccionServicio):
    def get_all_eleccion(self):
        try:
            all_eleccion = Eleccion.query.all()
            result = eleccion_schemas.dump(all_eleccion)
            return result
        except Exception as e:
            logger.error(f'Error al obtener todas las elecciones: {str(e)}')
            raise e
    
    def get_candidatos_by_eleccion(self, id_eleccion):
        try:
            all_candidatos = db.session.query(
                Candidato.nombres, 
                Candidato.apellido_paterno, 
                Candidato.apellido_materno, 
                ListaCandidato.nombre, 
                Candidato.id
            ).join(
                ListaCandidato, ListaCandidato.id_lista == Candidato.id_lista_candidato
            ).filter(
                ListaCandidato.id_eleccion == id_eleccion
            ).all()
            result = [{"Candidato": '%s %s %s' % (tupla[0], tupla[1], tupla[2]), "Lista": tupla[3], "id_candidato": tupla[4]} for tupla in all_candidatos]
            return result
        except Exception as e:
            logger.error(f'Error al obtener los candidatos por elección: {str(e)}')
            raise e
    
    def get_lista_by_eleccion(self, id_eleccion):
        try:
            all_listas = db.session.query(
                ListaCandidato.nombre, 
                ListaCandidato.id_lista
            ).filter(
                ListaCandidato.id_eleccion == id_eleccion
            ).all()
            result = [{"nombre": tupla[0], "id_lista": tupla[1]} for tupla in all_listas]
            return result
        except Exception as e:
            logger.error(f'Error al obtener las listas por elección: {str(e)}')
            raise e
    
    def get_all_eleccion_abiertas(self):
        try:
            all_eleccion = Eleccion.query.filter(Eleccion.estado == "abierto").all()
            result = eleccion_schemas.dump(all_eleccion)
            return result
        except Exception as e:
            logger.error(f'Error al obtener todas las elecciones abiertas: {str(e)}')
            raise e

    def insert_eleccion(self, eleccion):
        try:
            db.session.add(eleccion)
            db.session.commit()
            logger.info(f'Elección insertada correctamente: {eleccion}')
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error al insertar la elección: {str(e)}')
            raise e

    def votar(self, id_lista, id_elector):
        try:
            voto = Voto(id_elector, id_lista)
            db.session.add(voto)
            db.session.commit()
            logger.info(f'Voto registrado correctamente: {voto}')
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error al registrar el voto: {str(e)}')
            raise e

    def get_elector_by_email(self, email):
        try:
            elector = Elector.query.filter_by(correo=email).first()
            return elector
        except Exception as e:
            logger.error(f'Error al obtener el elector por email: {str(e)}')
            raise e

    def get_voto_by_elector(self, id_elector):
        try:
            voto = db.session.query(Elector.nombres).join(Voto, Elector.id == Voto.id_elector).filter(Elector.id == id_elector).all()
            result = [{"nombre": tupla[0]} for tupla in voto]
            return result
        except Exception as e:
            logger.error(f'Error al obtener el voto del elector: {str(e)}')
            raise e
        
        
class CandidatoServicioImpl(ICandidatoServicio):
    def get_candidatos_denegados(self):
        candidatos = Candidato.query \
            .filter(Candidato.denegado == True) \
            .all()
        result = []
        for candidato in candidatos:
            candidato_data = candidato_schema.dump(candidato)
            result.append(candidato_data)

        return result

    def get_candidatos_inscritos(self):
        candidatos = Candidato.query \
            .filter(Candidato.denegado == False) \
            .all()

        result = []
        for candidato in candidatos:
            candidato_data = candidato_schema.dump(candidato)
            result.append(candidato_data)

        return result


class ListaServicioImpl(IListaServicio):
    def obtener_listas_pendientes(self):
        listas = ListaCandidato.query.all()
        resultado = []
        
        for lista in listas:
            lista_info = {
                'id_lista': lista.id_lista,
                'nombre': lista.nombre,
                'estado': lista.estado.value,
                'id_eleccion': lista.id_eleccion,
                'propuestas': [{'descripcion': propuesta.descripcion} for propuesta in lista.propuestas],
                'candidatos': [{'nombre': f"{candidato.nombres} {candidato.apellido_paterno} {candidato.apellido_materno}"} for candidato in lista.candidatos]
            }
            
            resultado.append(lista_info)
        
        return resultado

