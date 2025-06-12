from app import create_app, db
import app.models  # 只导入模块，不直接导入 Patient
print("models模块导入成功")
from sqlalchemy import text

app = create_app()

with app.app_context():
    with db.engine.connect() as connection:
        result = connection.execute(text("SELECT DATABASE();"))
        print("当前连接数据库:", result.fetchone())


    db.create_all()
    print("数据库和表已创建成功！")
