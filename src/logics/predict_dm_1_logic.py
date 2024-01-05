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
        y_data_dto=Predict_dm_1_repository.predict_dm_1(x_data_dto=x_data_dto)
        return y_data_dto
