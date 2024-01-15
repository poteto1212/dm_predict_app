from pydantic import BaseModel

class Predict_dm_1_request(BaseModel):
  height: float
  bw :float
  fbs :float
  glc_3_auc :float
  ins_plasma_auc :float
  glc_css :float