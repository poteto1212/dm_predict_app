from fastapi import FastAPI
from pydantic import BaseModel
from dto.predict_dm_1_dto import Predict_dm_1_dto
from logics.predict_dm_1_logic import Predict_dm_1_logic

class Body(BaseModel):
  bw :float
  fbs :float
  glc_3_auc :float
  glc_plasma_auc :float
  glc_css :float
  
app = FastAPI()

@app.post("/predict/")
def predict_dm_1(body: Body):
  
  x_data_dto = Predict_dm_1_dto(
                bw=body.bw,
                fbs=body.fbs,
                glc_3_auc=body.glc_3_auc,
                glc_plasma_auc=body.glc_plasma_auc,
                glc_css=body.glc_css 
                )

  y_data_dto = Predict_dm_1_logic.predict_dm_1(x_data_dto=x_data_dto)
  
  return {"Preduct": y_data_dto.load_dm()}