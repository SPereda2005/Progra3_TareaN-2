from sqlalchemy.orm import Session
from . import models, schemas

def create_vuelo(db: Session, vuelo: schemas.VueloCreate):
    db_vuelo = models.Vuelo(**vuelo.dict())
    db.add(db_vuelo)
    db.commit()
    db.refresh(db_vuelo)
    return db_vuelo

def get_vuelos(db: Session):
    return db.query(models.Vuelo).order_by(models.Vuelo.prioridad.desc(), models.Vuelo.hora_despegue).all()

def update_vuelo_estado(db: Session, vuelo_id: int, nuevo_estado: str):
    vuelo = db.query(models.Vuelo).filter(models.Vuelo.id == vuelo_id).first()
    if vuelo:
        vuelo.estado = nuevo_estado
        db.commit()
        db.refresh(vuelo)
        return vuelo
    return None

def delete_vuelo(db: Session, vuelo_id: int):
    vuelo = db.query(models.Vuelo).filter(models.Vuelo.id == vuelo_id).first()
    if vuelo:
        db.delete(vuelo)
        db.commit()
        return True
    return False
