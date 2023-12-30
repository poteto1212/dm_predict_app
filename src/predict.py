import pickle
import numpy as np

#予測処理をモジュール化する
class Predict:
    @staticmethod
    def df_predict_logistic(x_data_list):
        model_path = "./model/dm_predict_model.pkle"
        x_data_np = np.array([x_data_list])
        with open(model_path, mode='rb') as fp:
            model = pickle.load(fp)
        return model.predict(x_data_np)[0]