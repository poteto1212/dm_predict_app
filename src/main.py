from fastapi import FastAPI 
app = FastAPI()

from requests.predict_dm_1_request import Predict_dm_1_request
from dto.predict_dm_1_dto import Predict_dm_1_dto
from logics.predict_dm_1_logic import Predict_dm_1_logic

@app.post("/predict_dm_1/")
def predict_dm_1(body: Predict_dm_1_request):
  
  x_data_dto = Predict_dm_1_dto(
                height= body.height,
                bw=body.bw,#身長受け取り
                fbs=body.fbs,
                glc_3_auc=body.glc_3_auc,
                glc_plasma_auc=body.glc_plasma_auc,
                glc_css=body.glc_css 
                )

  y_data_dto = Predict_dm_1_logic.predict_dm_1(x_data_dto=x_data_dto)
  
  return {
    "Category":str(y_data_dto.load_category()),
    "Preduct": y_data_dto.load_dm_predict()}