from app import db
## 病人
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
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birthdate": self.birthdate.isoformat() if self.birthdate else None,
            "phone": self.phone,
            "address": self.address
        }
    
## 医生
class Doctor(db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    specialization = db.Column(db.String(100))
    phone = db.Column(db.String(20))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "specialization": self.specialization,
            "phone": self.phone
        }