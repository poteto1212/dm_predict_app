from fastapi.security import HTTPBasicCredentials
from fastapi import HTTPException,status
from datetime import datetime, timedelta

import sys
sys.path.append("../src")
from modules.security_modules import Security_modules

import sys
sys.path.append("../src")
from repositories.session_repository import Session_repository
#認証周りのロジックを記載
class Session_logic:
    
    def __init__(self):
        self.session = {}
    #ユーザーを認証する
    def authenticate_user(self, input_usernmae:str,input_password:str):#Jason形式で受け取るように修正
        user_name_record,password_record = Session_repository.get_user_password(user_name=input_usernmae)#ここにjsonを流し込む
        check_passwood_ = Security_modules.check_password(
            plain_password = input_password,
            hashed_password = password_record
        )
        
        #ユーザー名が存在しないもしくはパスワードが誤りのとき
        if not user_name_record or not check_passwood_:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,#401エラーを返す
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        #セッションを更新する
        #メモリ的に厳しそうであれば
        self.session.update(
            {
                user_name_record:
                    {"last_login" : datetime.now()}
            }
        )
        #ユーザー名を返す
        return user_name_record
    
    #不用なセッションを削除する
    # def drop_session
    
    #セッションを更新する
    
    def check_session(self):
        if "last_login" in self.session:
            #最終ログインから30分経過しているかの確認
            if datetime.now() - self.session["last_login"] > timedelta(minutes=30):
                #30分経過していたら再ログインを促す
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,#401エラーを返す
                    detail="Session expired. Please login again.",
                )

    