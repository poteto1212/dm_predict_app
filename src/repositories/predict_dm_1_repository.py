import sys
sys.path.append("../src")
from dto.predict_dm_1_dto import Predict_dm_1_dto
from dto.ans_dm_1_dto import Ans_dm_1_dto
from predicts.predict import Predict

#役割
# 1. 機械学習モデルの呼び出し 2. データベースへのアクセス
class Predict_dm_1_repository:
    @staticmethod
    def predict_dm_1(predict_dm_1_dto: Predict_dm_1_dto)->Ans_dm_1_dto:
        
        #ロジスティクス回帰モデルの呼び出し
        predict_val = Predict.dm_1_predict_logistic(
            relative_bw = predict_dm_1_dto.load_rlative_bw(),
            fbs = predict_dm_1_dto.load_fbs(),
            glc_3_auc = predict_dm_1_dto.load_glc_3_auc(),
            glc_plasma_auc = predict_dm_1_dto.load_glc_plasma_auc(),
            glc_css = predict_dm_1_dto.load_glc_css()
        )
        #TODO 結果のデータベースへの一時保管
        
        ans_dm_1_dto=Ans_dm_1_dto(predict_val=predict_val)
        return ans_dm_1_dto
