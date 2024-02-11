import pandas as pd
from sqlalchemy.orm import sessionmaker

import sys
sys.path.append("../src")
from modules.security_modules import Security_modules
from settings import engin
from models.user_model import User_model
from models.admin_model import Admin_model
 
class User_seed:
    @staticmethod
    def insert_test_user():
        print("userテーブルにテストデータを登録する")
        df=pd.read_csv("seeds/datasets/users/users_seed.csv")
        #ハッシュ化対象カラム
        column_to_hash = 'password'
        df[column_to_hash] = df[column_to_hash].apply(Security_modules.hash_value)
        df.to_sql("users",engin,if_exists="append",index=False)
    
    @staticmethod
    def delete_test_user():
        print("userテーブルからテストデータを削除するx")  
        session = sessionmaker(bind=engin)()
        
        session.query(Admin_model).delete()
        session.query(User_model).delete()
        
        session.commit()
        session.close()
        

