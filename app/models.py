from app import db
from datetime import datetime

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
    gender = db.Column(db.Integer)
    roll = db.Column(db.Integer)
    adress = db.Column(db.String(50))
    work_year = db.Column(db.Integer)
    department_id = db.Column(db.Integer)
    position_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment='更新时间')
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "specialization": self.specialization,
            "phone": self.phone,
            "gender" : self.phone,
            "roll" : self.roll,
            "adress": self.adress,
            "work_year": self.work_year
        }
        
# 科室
class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True, comment='科室名称，例如 内科、外科')
    code = db.Column(db.String(20), unique=True, nullable=False, comment='科室编号，用于管理')
    floor = db.Column(db.String(20), comment='所在楼层或区域')
    phone = db.Column(db.String(20), comment='联系电话')
    description = db.Column(db.String(255), comment='科室简介或职责说明')
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment='更新时间')

    def __repr__(self):
        return f'<Department {self.name}>'

# 职位    
class Position(db.Model):
    __tablename__ = 'positions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True, comment='职位名称，例如 主任医师、护士长')
    code = db.Column(db.String(20), unique=True, nullable=False, comment='职位编号，用于内部识别')
    level = db.Column(db.Integer, default=1, comment='职位等级，数值越高等级越高')
    description = db.Column(db.String(255), comment='职位职责或简介')
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment='更新时间')

    def __repr__(self):
        return f'<Position {self.name}>'
    
    
#病例
class Case(db.Model):
    __tablename__ = 'cases'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False, comment='关联患者ID')
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False, comment='主诊医生ID')
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False, comment='就诊科室')
    diagnosis = db.Column(db.String(255), comment='初步诊断')
    status = db.Column(db.String(32), default='进行中', comment='状态，如进行中、已完成、已转诊')
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='病例创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment='最后更新时间')

    # relationships（可选，方便ORM使用）
    patient = db.relationship('Patient', backref='cases')
    doctor = db.relationship('Doctor', backref='cases')
    department = db.relationship('Department', backref='cases')

    def __repr__(self):
        return f'<Case ID={self.id} PatientID={self.patient_id}>'

#就诊记录
class CaseRecord(db.Model):
    __tablename__ = 'case_records'

    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('cases.id'), nullable=False, comment='关联的病例ID')
    record_type = db.Column(db.String(32), nullable=False, comment='记录类型，如初诊、复诊、检查、治疗')
    content = db.Column(db.Text, nullable=False, comment='记录内容，如诊断描述、治疗方法等')
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='记录创建时间')

    # relationship
    case = db.relationship('Case', backref='records')

    def __repr__(self):
        return f'<CaseRecord ID={self.id} Type={self.record_type}>'