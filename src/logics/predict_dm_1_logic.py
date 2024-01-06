import sys
sys.path.append("../src")
from dto.predict_dm_1_dto import Predict_dm_1_dto
from dto.ans_dm_1_dto import Ans_dm_1_dto
from repositories.predict_dm_1_repository import Predict_dm_1_repository

#役割
# 1. リクエストデータの整形 2. リポジトリの呼び出し
class Predict_dm_1_logic:
    @staticmethod
    def predict_dm_1(x_data_dto: Predict_dm_1_dto)->Ans_dm_1_dto:
        
        #身長から基準体重の算出
        height=x_data_dto.load_height()
        base_bw = 22*((height/100)**2)
        bw = x_data_dto.load_bw()
        relative_bw = bw - base_bw
        x_data_dto.update_rlative_bw(relative_bw=relative_bw)

        #体重を相対体重に変換する
        y_data_dto=Predict_dm_1_repository.predict_dm_1(x_data_dto=x_data_dto)
        
        #予測結果に基づいて判定
        if y_data_dto.load_category() == 1:
            y_data_dto.update_dm(dm_predict="糖尿病の可能性が高い")
        elif y_data_dto.load_category() == 0:
            y_data_dto.update_dm(dm_predict="糖尿病の可能性は低い")
        
        return y_data_dto
