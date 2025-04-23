from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from . import models, crud, schemas

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base de datos si no existe
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/vuelos/")
def crear_vuelo(vuelo: schemas.VueloCreate, db: Session = Depends(get_db)):
    return crud.create_vuelo(db=db, vuelo=vuelo)

@app.get("/vuelos/")
def obtener_vuelos(db: Session = Depends(get_db)):
    return crud.get_vuelos(db=db)

@app.put("/vuelos/{vuelo_id}")
def actualizar_estado_vuelo(vuelo_id: int, estado: str, db: Session = Depends(get_db)):
    vuelo = crud.update_vuelo_estado(db=db, vuelo_id=vuelo_id, nuevo_estado=estado)
    if vuelo:
        return vuelo
    raise HTTPException(status_code=404, detail="Vuelo no encontrado")

@app.delete("/vuelos/{vuelo_id}")
def eliminar_vuelo(vuelo_id: int, db: Session = Depends(get_db)):
    if not crud.delete_vuelo(db=db, vuelo_id=vuelo_id):
        raise HTTPException(status_code=404, detail="Vuelo no encontrado")
    return {"message": "Vuelo eliminado"}
