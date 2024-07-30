import logging

from app.models.Elector import Elector
from app import db
from app.services.IPersonaServicio import ElectorService

logger = logging.getLogger(__name__)

class ElectorServiceImpl(ElectorService):
    def get_elector_by_id(self, id):
        try:
            return Elector.query.get(id)
        except Exception as e:
            logger.error(f'Error al obtener el elector por ID: {str(e)}')
            raise e

    def create_elector(self, elector_modelo, contrasena:str):
        elector = Elector(
            nombres=elector_modelo.nombres,
            apellido_paterno=elector_modelo.apellido_paterno,
            apellido_materno=elector_modelo.apellido_materno,
            fecha_nacimiento=elector_modelo.fecha_nacimiento,
            usuario=elector_modelo.usuario,
            contrasena=contrasena,
            correo=elector_modelo.correo
        )
        try:
            db.session.add(elector)
            db.session.commit()
            logger.info(f'Elector creado correctamente: {elector}')
            return elector
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error al crear el electbor: {str(e)}')
            raise e

    def update_elector(self, elector: Elector):
        try:
            db.session.merge(elector)
            db.session.commit()
            logger.info(f'Elector actualizado correctamente: {elector}')
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error al actualizar el elector: {str(e)}')
            raise e

    def delete_elector(self, elector: Elector):
        try:
            db.session.delete(elector)
            db.session.commit()
            logger.info(f'Elector eliminado correctamente: {elector}')
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error al eliminar el elector: {str(e)}')
            raise e
        
