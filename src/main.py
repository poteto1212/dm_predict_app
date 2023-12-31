from fastapi import FastAPI
from pydantic import BaseModel
import predict

class Body(BaseModel):
  bw :float
  fbs :float
  glc_3_auc :float
  glc_plasma_auc :float
  glc_css :float
  
app = FastAPI()

@app.post("/predict/")
def predict_dm_1(body: Body):
  x_data_list = [body.bw,
                 body.fbs,
                 body.glc_3_auc,
                 body.glc_plasma_auc,
                 body.glc_css]
  y_data_answer=predict.Predict.df_predict_logistic(x_data_list)
  
  return {"Preduct": str(y_data_answer)}