from database import db # se importa la instancia de la base de datos para poder ser utilizada en otros archivos

class User(db.Model): #tenemos una clase que es hace la tabla de usuarios 
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(10), default='user')
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', is_active={self.is_active})>"

