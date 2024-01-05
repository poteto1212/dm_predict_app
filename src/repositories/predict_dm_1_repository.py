import sys
sys.path.append("../src")
from dto.predict_dm_1_dto import Predict_dm_1_dto
from dto.ans_dm_1_dto import Ans_dm_1_dto
from predicts.predict import Predict

#役割
# 1. 機械学習モデルの呼び出し 2. データベースへのアクセス
class Predict_dm_1_repository:
    @staticmethod
    def predict_dm_1(x_data_dto: Predict_dm_1_dto)->Ans_dm_1_dto:
        #ロジスティクス回帰モデルの呼び出し
        y_data=Predict.df_predict_logistic(x_data_dto = x_data_dto)
        #結果のデータベースへの一時保管
        #保管処理を記載する
             
        #オブジェクトで返す
        y_data_dto=Ans_dm_1_dto(dm=str(y_data))
        return y_data_dto
