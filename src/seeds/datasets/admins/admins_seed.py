from sqlalchemy.orm import sessionmaker
from settings import engin
from models.admin_model import Admin_model
from models.user_model import User_model
import sys
sys.path.append("../src")
from settings import engin

class Admin_seed:
    @staticmethod
    def insert_test_admin(user_name: str):
        print("指定したidのユーザーを管理者テーブルに追加")
        session = sessionmaker(bind=engin)()
        
        #管理者ユーザーのidを取得
        user_id = session.query(
            User_model.id
        ).filter(User_model.user_name == user_name)
        
        new_record = Admin_model(
            user_id = user_id
        )
        session.add(new_record)
        
        session.commit()
        session.close()