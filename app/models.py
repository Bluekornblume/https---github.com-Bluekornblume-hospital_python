from app import db

class Patient(db.Model):
    __tablename__ = 'patients'

    print("Patient 模型被加载了")

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10))
    birthdate = db.Column(db.Date)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))

    

    def __repr__(self):
        return f'<Patient {self.name}>'