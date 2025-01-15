from ._database import db

class Paquete(db.Model):
    __tablename__ = "paquetes"

    id = db.Column(db.Integer, primary_key=True,)
    description = db.Column(db.String, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String, default='Pendiente')

    def __repr__(self):
        return f"<Paquete(id={self.id}, description='{self.description}', peso={self.peso}, estado='{self.estado}')>"



