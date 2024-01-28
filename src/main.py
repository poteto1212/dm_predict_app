from fastapi import FastAPI,Depends
app = FastAPI()

from requests.predict_dm_1_request import Predict_dm_1_request
from dto.predict_dm_1_dto import Predict_dm_1_dto
from logics.predict_dm_1_logic import Predict_dm_1_logic
from starlette.middleware.cors import CORSMiddleware 
from datetime import datetime
import os

origins = [
  os.environ['FRONT_URL']
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,   # 追記により追加
  allow_methods=["*"],      # 追記により追加
  allow_headers=["*"]       # 追記により追加
)

from logics.session_logic import Session_logic
from fastapi.security import  HTTPBasicCredentials,HTTPBasic

security = HTTPBasic()
session_logic = Session_logic()

#ログインAPI
@app.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
  user = session_logic.authenticate_user(credentials)
  session_logic.session.update({"username": user["username"], "last_login": datetime.now()})
  return {"message": "Login successful"}

# ホームAPI
@app.get("/home")
def home(session: dict = Depends(session_logic.check_session), credentials: HTTPBasicCredentials = Depends(security)):
    return {"message": f"Welcome, {session_logic.session['username']}!"}

#ログアウトAPI
# ログアウトAPI
@app.post("/logout")
def logout(session: dict = Depends(session_logic.check_session), credentials: HTTPBasicCredentials = Depends(security)):
    session_logic.session.clear()
    return {"message": "Logout successful"}

#糖尿病予測API
@app.post("/predict_dm_1/")
def predict_dm_1(body: Predict_dm_1_request):
  
  predict_dm_1_dto = Predict_dm_1_dto(
                height= body.height,
                bw=body.bw,
                fbs=body.fbs,
                glc_3_auc=body.glc_3_auc,
                ins_plasma_auc=body.ins_plasma_auc,
                glc_css=body.glc_css 
                )

  ans_dm_1_dto = Predict_dm_1_logic.predict_dm_1(predict_dm_1_dto=predict_dm_1_dto)
  
  return {
    "predict_val":str(ans_dm_1_dto.load_predict_val()),
    "result": ans_dm_1_dto.load_result()}