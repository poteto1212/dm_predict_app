import sys
sys.path.append("../src")
from dto.predict_dm_1_dto import Predict_dm_1_dto
from dto.ans_dm_1_dto import Ans_dm_1_dto
from repositories.predict_dm_1_repository import Predict_dm_1_repository

#役割
# 1. リクエストデータの整形 2. リポジトリの呼び出し
class Predict_dm_1_logic:
    @staticmethod
    def predict_dm_1(predict_dm_1_dto: Predict_dm_1_dto)->Ans_dm_1_dto:
        
        #身長から基準体重の算出
        height=predict_dm_1_dto.load_height()
        #体重を相対体重に変換する
        base_bw = 22*((height/100)**2)
        bw = predict_dm_1_dto.load_bw()
        predict_dm_1_dto.update_rlative_bw(relative_bw=bw - base_bw)

        ans_dm_1_dto=Predict_dm_1_repository.predict_dm_1(predict_dm_1_dto=predict_dm_1_dto)
        
        #予測結果に基づいて判定
        if ans_dm_1_dto.load_predict_val() == 1:
            ans_dm_1_dto.update_result(reult ="糖尿病の可能性が高い")
        elif ans_dm_1_dto.load_predict_val() == 0:
            ans_dm_1_dto.update_result(reult ="糖尿病の可能性は低い")
        
        return ans_dm_1_dto
