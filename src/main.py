from fastapi import FastAPI
import predict
app = FastAPI()

@app.get("/")
def read_root():
  x_data_list = [1.11,360,1246,124,442]
  y_data_answer=predict.Predict.df_predict_logistic(x_data_list)
  return {"Hello": str(y_data_answer)}