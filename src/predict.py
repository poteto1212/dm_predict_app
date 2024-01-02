import pickle
import numpy as np
import pandas as pd

#予測処理をモジュール化する
class Predict:
    @staticmethod
    def df_predict_logistic(x_data_list):
        model_path = "./learning_model/dm_predict_model.pkle"
        x_data_df = pd.DataFrame({
            "相対体重":[x_data_list[0]],
            "空腹時血糖":[x_data_list[1]],
            "3時間血漿グルコース曲線下の面積":[x_data_list[2]],
            "血漿インスリン曲線下面積":[x_data_list[3]],
            "定常状態血糖":[x_data_list[4]],      
        })
        with open(model_path, mode='rb') as fp:
            model = pickle.load(fp)
        return model.predict(x_data_df)[0]