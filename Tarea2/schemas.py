from pydantic import BaseModel

class VueloBase(BaseModel):
    nombre: str
    destino: str
    prioridad: int
    estado: str
    hora_despegue: str

class VueloCreate(VueloBase):
    pass

class Vuelo(VueloBase):
    id: int

    class Config:
        orm_mode = True
