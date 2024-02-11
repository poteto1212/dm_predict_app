from sqlalchemy.orm import sessionmaker

#認証周りに必要な情報をDBから取ってくる
import sys
sys.path.append("../src")
from models.user_model import User_model
from settings import engin

class Session_repository:
    @staticmethod
    def get_user_password(user_name: str):
        
        session = sessionmaker(bind=engin)()
        
        records = session.query(
            User_model.user_name,
            User_model.password                      
            ).filter(User_model.user_name == user_name).one_or_none()
        
        if records == None:
            user_name_record = None
            password_record = None
            return user_name_record , password_record
        
        user_name_record , password_record = records
             
        # session.commit() ←必要性検討　検索しているだけだからいらない？
        session.close()
        
        return user_name_record , password_record
