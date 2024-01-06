from fastapi import FastAPI 
app = FastAPI()

from requests.predict_dm_1_request import Predict_dm_1_request
from dto.predict_dm_1_dto import Predict_dm_1_dto
from logics.predict_dm_1_logic import Predict_dm_1_logic

@app.post("/predict_dm_1/")
def predict_dm_1(body: Predict_dm_1_request):
  
  predict_dm_1_dto = Predict_dm_1_dto(
                height= body.height,
                bw=body.bw,
                fbs=body.fbs,
                glc_3_auc=body.glc_3_auc,
                glc_plasma_auc=body.glc_plasma_auc,
                glc_css=body.glc_css 
                )

  ans_dm_1_dto = Predict_dm_1_logic.predict_dm_1(predict_dm_1_dto=predict_dm_1_dto)
  
  return {
    "predict_val":str(ans_dm_1_dto.load_predict_val()),
    "result": ans_dm_1_dto.load_result()}