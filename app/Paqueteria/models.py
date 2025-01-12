from Paqueteria.database import db

class paquete(db.Model):
    __tablename__ = "paquetes"

    id = db.Column(db.Integer, primary_key=True,)
    description = db.Column(db.String, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String, default='Pendiente')

    def __repr__(self):
        return f"<paquete(id={self.id}, description='{self.description}', peso={self.peso}, estado='{self.estado}')>"



