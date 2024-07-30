
## Buenas Prácticas de Clean Code


- **1.Nombre claros y descriptivos:** Los nombres como `Propuesta`, `id_candidato`, y `propuesta` son claros y descriptivos, lo que facilita entender el propósito de cada modelo y campo.
- **2.Notacion variables** Los nombres de métodos como `get_candidatos_con_propuestas` ustilizan la notacion snake_case.
- **3. Espacios e indentacion** No dejar espacios entre parentesis o corchetes, respetar la indentacion, se recomienda dejar espacios antes y despues de una asiganacion que no sea como argumento.
```python
class Propuesta(db.Model):
    __tablename__ = 'propuesta'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_candidato = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)
    propuesta = db.Column(db.Text, nullable=False)
    
```
```python
    def get_candidatos_con_propuestas(self):
       
        candidatos = Candidato.query.options(db.joinedload(Candidato.propuestas)).all()
        
        result = []
        for candidato in candidatos:
            candidato_data = candidato_schema.dump(candidato)
            propuestas_data = propuesta_schema.dump(candidato.propuestas, many=True)
            candidato_data['propuestas'] = propuestas_data
            result.append(candidato_data)
        
        return result
```
- **4. Jerarquia de las importaciones** El orden de en el grupo de importaciones debe tener primero a los modulos estandar, luego los terceros y por ultimo los del proyecto. El orden alfabetico es opcional'

```python
    import logging

    from flask import render_template, Blueprint, request, jsonify, session, redirect, url_for, make_response

    from app.models.Elector import Elector
    from app.models.Eleccion import Eleccion
    from app.models.ListaCandidato import ListaCandidato
    from app.models.Candidato import Candidato
    from app.services.PersonaServicioImpl import ElectorServiceImpl
    from app.services.EleccionServicioImpl import EleccionServicioImpl
```

- **5. Estilo y Estructura**: Las separacion entre las clases y funciones debe ser de 2 espacios en blanco y , un espacio en blanco entre los metodos
```python
class EleccionServicioImpl(IEleccionServicio):
    def get_all_eleccion(self):
        all_eleccion = Eleccion.query.all()
        result = eleccion_schemas.dump(all_eleccion)
        return result
    
    def get_candidatos_by_eleccion(self, id_eleccion):
        all_candidatos = db.session.query(Candidato.nombres, Candidato.apellido_paterno, Candidato.apellido_materno, ListaCandidato.nombre, Candidato.id).join(ListaCandidato, ListaCandidato.id_lista == Candidato.id_lista_candidato).filter(ListaCandidato.id_eleccion == id_eleccion).all()
        result = [{"Candidato": '%s %s %s' % (tupla[0], tupla[1], tupla[2]), "Lista": tupla[3], "id_candidato": tupla[4]} for tupla in all_candidatos]
        return result
    
    def get_all_eleccion_abiertas(self):
        all_eleccion = Eleccion.query.filter(Eleccion.estado == "abierto").all()
        result = eleccion_schemas.dump(all_eleccion)
        return result
    
    def insert_eleccion(self, eleccion):
        db.session.add(eleccion)
        db.session.commit()
```

## Principios SOLID

### 1.Single Responsibility Principle (SRP) - Principio de Responsabilidad Única

- La clase **Candidato** es una  clase que tiene una responsabilidad clara y específica. A diferencia de otras clases similares como el de **Elector**
```python
class Candidato(db.Model):
    __tablename__ = 'candidato'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    id_lista_candidato = db.Column(db.Integer, db.ForeignKey('lista_candidato.id_lista'),nullable=True)
```
### 2.Open/Closed Principle (OCP) - Principio de Abierto/Cerrado

- El código está diseñado para ser extendido sin modificar alguna clase o metodo, manteniendo su codigo original.

### 3.Interface Segregation Principle - ISP 
- Tenemos nuestra interfaz **ElectroService** que posee relativamente pocos metodos, evitando una division en otras interfaces.

```python
class ElectorService(ABC):
    @abstractmethod             
    def get_elector_by_id(self, id):
        pass

    @abstractmethod
    def create_elector(self, elector):
        pass

    @abstractmethod
    def update_elector(self, elector):
        pass

    @abstractmethod
    def delete_elector(self, elector):
        pass
```