from app import create_app, db
from app.models import Doctor, Patient  # 只导入模块，不直接导入 Patient
print("models模块导入成功")
from sqlalchemy import text

app = create_app()

with app.app_context():
    with db.engine.connect() as connection:
        result = connection.execute(text("SELECT DATABASE();"))
        print("当前连接数据库:", result.fetchone())


    db.drop_all()
    db.create_all()

    # 插入测试数据
    doctor = Doctor(name="张医生", specialization="内科", phone="12345678")
    db.session.add(doctor)
    db.session.commit()
    print("数据库和表已创建成功！")
