from sqlalchemy.orm import sessionmaker
from settings import engin
from models.admin_model import Admin_model
import sys
sys.path.append("../src")
from settings import engin

class Admin_seed:
    @staticmethod
    def insert_test_admin(user_id:int):
        print("指定したidのユーザーを管理者テーブルに追加")
        session = sessionmaker(bind=engin)()
        
        new_record = Admin_model(
            user_id = user_id
        )
        session.add(new_record)
        
        session.commit()
        session.close()