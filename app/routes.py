
from app.models import Patient, Doctor
from flask import Blueprint, jsonify, request
from app import db
from datetime import datetime

bp = Blueprint('api', __name__)

@bp.route('/')
def index():
    return "欢迎来到病院管理システム！"

@bp.route('/patient', methods = ['GET'])
def get_patients():
    patients = Patient.query.all()
    patients_list = [patient.to_dict() for patient in patients]
    return jsonify(patients_list)

@bp.route('/patient/insert', methods = ['POST'])
def insert_patient():
    data = request.get_json()
    

    name = data.get('name')
    if not name:
        return jsonify({"error" : "请输入姓名"}), 400
    
    birthdate_str = data.get('birthdate')
    birthdate_date = None
    if birthdate_str != None:
        try:
            birthdate_date = datetime.strptime(birthdate_str, "%Y-%m-%d")
        except ValueError:
            return jsonify({"日期格式应为 YYYY-MM-DD"}), 400
        
    new_patient = Patient(
        name = name,
        gender = data.get("gender"),
        birthdate = birthdate_date,
        phone = data.get("phone"),
        address = data.get("address")
    )
        
    try:
        db.session.add(new_patient)
        db.session.commit()
        print("✅ 数据成功插入：", new_patient)
    except Exception as e:
        db.session.rollback()
        print("❌ 数据库提交失败：", str(e))
        return jsonify({"error": "数据库写入失败", "details": str(e)}), 500

    return jsonify({
        "message": "新增病人成功",
        "patient": new_patient.to_dict()
    }), 201
    

@bp.route("/patient/<int:patient_id>", methods = ['GET'])
def get_by_id(patient_id):
    patient = Patient.query.get(patient_id)
    
    return jsonify(patient.to_dict())

@bp.route("/patient/<int:patient_id>", methods = ['PUT'])
def update(patient_id):
    # 🔹 1. 获取 URL 中的 ID 参数
    update_patient = Patient.query.get(patient_id)
    if not update_patient:
        return jsonify({"error": "未找到该病人"}), 404
    
    
    data = request.get_json()
    
    #名前チェック
    name = data.get("name")
    if not name:
        return jsonify({"error" : "名前を入力してください"}), 400
    
    #誕生日チェック
    birthdate_str = data.get("birthdate")
    if birthdate_str:
        try:
            update_patient.birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        except ValueError:
            return jsonify({"error" : "正しい誕生日を入力してください。"}), 400
    
    
    update_patient.name = name
    update_patient.gender = data.get("gender")
    update_patient.phone = data.get("phone")
    update_patient.address = data.get("address")
    
    db.session.commit()
    # 🔹 6. 返回响应
    return jsonify({
        "message": "更新成功",
        "patient": update_patient.to_dict()
    })