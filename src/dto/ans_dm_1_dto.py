#DM1の目的変数オブジェクト
class Ans_dm_1_dto:
    def __init__(self,
                 category: int,
):
        self.__category = category
        self.__dm_predict = None

    
    def load_category(self)->int:
        return self.__category
    
    def update_dm(self,dm_predict: str):
        self.__dm_predict = dm_predict
    
    def load_dm_predict(self) -> str:
        return self.__dm_predict
    
