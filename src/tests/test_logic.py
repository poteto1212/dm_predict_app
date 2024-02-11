from fastapi import HTTPException
import pytest

import datetime
import sys
sys.path.append("../src")

from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

#認証ロジックのテスト
from logics.session_logic import Session_logic
session_logic = Session_logic()


def test_authenticate_user():
    print("ユーザー1によるログイン処理")
    #呼び出し
    user_name_record = session_logic.authenticate_user(
        input_username="test.admin@1212",
        input_password="pass_admin"
    )
    
    login_session = session_logic.session
    print("ユーザー名が帰る")
    assert user_name_record == "test.admin@1212"
    
    print("セッションに登録されている")
    assert "test.admin@1212" in login_session 
    
    print("ログイン日時はdatetime型")
    assert isinstance(login_session["test.admin@1212"]["last_login"],datetime.datetime)
    
    print("存在しないユーザーでログインするとエラー")
    with pytest.raises(HTTPException) as e:
        session_logic.authenticate_user(
        input_username="test.admin@112",
        input_password="pass_admin"
        )
        
    print("誤ったパスワードでログインするとエラー")
    with pytest.raises(HTTPException) as e:
        session_logic.authenticate_user(
        input_username="test.admin@1212",
        input_password="pass_admins"
        )