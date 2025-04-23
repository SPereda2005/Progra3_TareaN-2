from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vuelo(Base):
    __tablename__ = "vuelos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    destino = Column(String)
    prioridad = Column(Integer, default=0)  # Prioridad 0 es baja, 1 es alta (emergencia)
    estado = Column(String, default="programado")  # Programado, retrasado, cancelado
    hora_despegue = Column(String)  # Ejemplo: '2023-04-22 15:30'

    def __repr__(self):
        return f"<Vuelo(nombre={self.nombre}, destino={self.destino}, prioridad={self.prioridad}, estado={self.estado})>"
