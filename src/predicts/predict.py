import sys
sys.path.append("../src")
from dto.predict_dm_1_dto import Predict_dm_1_dto

import pickle
import numpy as np
import pandas as pd

#予測処理をモジュール化する
class Predict:
    @staticmethod
    def dm_1_predict_logistic(
        relative_bw: float,
        fbs: float,
        glc_3_auc: float,
        ins_plasma_auc: float,
        glc_css: float
        
    )->int:
        model_path = "./predicts/learning_models/dm_1_predict_logistic_model.pkle"
        x_data_df = pd.DataFrame({
            "相対体重":[relative_bw],
            "空腹時血糖":[fbs],
            "3時間血漿グルコース曲線下の面積":[glc_3_auc],
            "血漿インスリン曲線下面積":[ins_plasma_auc],
            "定常状態血糖":[glc_css],      
        })
        with open(model_path, mode='rb') as fp:
            model = pickle.load(fp)
        return model.predict(x_data_df)[0]