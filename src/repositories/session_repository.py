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
        
        user_name_record,password_record = session.query(
            User_model.user_name,
            User_model.password                      
            ).filter(User_model.user_name == user_name).one_or_none()
               
        # session.commit() ←必要性検討　検索しているだけだからいらない？
        session.close()
        
        return user_name_record,password_record
    
# print(Session_repository.get_user_password("test.admin@1212"))
# Session_repository.get_user_data("test.admin@1212")