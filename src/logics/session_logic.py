from fastapi.security import HTTPBasicCredentials
from fastapi import HTTPException,status
from datetime import datetime, timedelta

import sys
sys.path.append("../src")
from repositories.session_repository import Session_repository
#認証周りのロジックを記載
class Session_logic:
    
    def __init__(self):
        self.session = {}
    #ユーザーを認証する
    def authenticate_user(self, credentials: HTTPBasicCredentials):
        user_name_record,password_record = Session_repository.get_user_password(credentials.username)#ここにjsonを流し込む
        input_password = credentials.password.encode('utf8')
        #ユーザー名が存在しないもしくはパスワードが誤りのとき
        if not user_name_record or password_record != input_password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,#401エラーを返す
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return user_name_record
    
    def check_session(self):
        if "last_login" in self.session:
            #最終ログインから30分経過しているかの確認
            if datetime.now() - self.session["last_login"] > timedelta(minutes=30):
                #30分経過していたら再ログインを促す
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,#401エラーを返す
                    detail="Session expired. Please login again.",
                )

    