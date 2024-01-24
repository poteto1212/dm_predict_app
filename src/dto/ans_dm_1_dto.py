#DM1の目的変数オブジェクト
class Ans_dm_1_dto:
    def __init__(self,
                 predict_val: int,
):
        self.__predict_val = predict_val
        self.__reult = None

    def load_predict_val(self)->int:
        return self.__predict_val
    
    def update_result(self,reult: str):
        self.__reult = reult
    
    def load_result(self) -> str:
        return self.__reult
    
