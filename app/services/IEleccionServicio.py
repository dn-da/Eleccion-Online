from abc import ABC, abstractmethod

class IEleccionServicio(ABC):
    @abstractmethod
    def get_all_eleccion(self):
        pass
    
    @abstractmethod
    def get_candidatos_by_eleccion(self, int):
        pass
    
    @abstractmethod
    def get_all_eleccion_abiertas(self):
        pass
    
    @abstractmethod
    def insert_eleccion(self, eleccion):
        pass
    
    @abstractmethod
    def get_elector_by_email(self, email):
        pass

class IVotoServicio(ABC):
    @abstractmethod
    def get_voto_by_elector(self, id_elector):
        pass 
    @abstractmethod
    def votar(self, id_lista, id_elector):
        pass
    
    @abstractmethod
    def get_all_votos(self):
        pass


class ICandidatoServicio(ABC):
    @abstractmethod
    def get_candidatos_denegados(self):
        pass
    
    @abstractmethod
    def get_candidatos_inscritos(self):
        pass


class IListaServicio(ABC):
    @abstractmethod
    def obtener_listas_pendientes(self):
        pass
    
    @abstractmethod
    def get_lista_by_eleccion(self, id_eleccion):
        pass