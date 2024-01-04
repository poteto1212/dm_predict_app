import sys
sys.path.append("../src")
from dto.predict_dm_1_dto import Predict_dm_1_dto

import pickle
import numpy as np
import pandas as pd

#予測処理をモジュール化する
class Predict:
    @staticmethod
    def df_predict_logistic(x_data_dto :Predict_dm_1_dto):
        model_path = "./learning_model/dm_predict_model.pkle"
        x_data_df = pd.DataFrame({
            "相対体重":[x_data_dto.load_bw()],
            "空腹時血糖":[x_data_dto.load_fbs()],
            "3時間血漿グルコース曲線下の面積":[x_data_dto.load_glc_3_auc()],
            "血漿インスリン曲線下面積":[x_data_dto.load_glc_plasma_auc()],
            "定常状態血糖":[x_data_dto.load_glc_css()],      
        })
        with open(model_path, mode='rb') as fp:
            model = pickle.load(fp)
        return model.predict(x_data_df)[0]