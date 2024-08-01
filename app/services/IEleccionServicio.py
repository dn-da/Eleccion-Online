from abc import ABC, abstractmethod

class IEleccionServicio(ABC):
    @abstractmethod
    def get_all_eleccion(self):
        pass    
    
    @abstractmethod
    def get_candidatos_by_eleccion(self, int):
        pass

    @abstractmethod
    def insert_eleccion(self, eleccion):
        pass
    
    @abstractmethod
    def get_elecciones_hechas_por_elector(self, id_elector):
        pass
    
    @abstractmethod
    def get_elecciones_hechas_por_elector(self, id_elector):
        pass

    @abstractmethod
    def get_all_elecciones(self):
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
    
    @abstractmethod
    def get_cant_votos_by_eleccion(self, id_eleccion):
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
    def obtener_listas(self):
        pass
    
    @abstractmethod
    def get_lista_aprobada_by_eleccion(self, id_eleccion):
        pass
    
    @abstractmethod
    def get_lista_por_eleccion(self, id_eleccion):
        pass
    
    @abstractmethod
    def aprobar_lista(self, id_lista):
        pass
    
    @abstractmethod
    def desaprobar_lista(self, id_lista):
        pass
    
    @abstractmethod
    def get_lista_by_id(self, id_lista):
        pass
    
    @abstractmethod
    def obtener_listas_aprobadas(self):
        pass
    
    @abstractmethod
    def get_all_eleccion_abiertas(self):
        pass