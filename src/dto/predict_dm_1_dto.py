#DM1の説明変数オブジェクト
class Predict_dm_1_dto:
    def __init__(self,
                 height: float,
                 bw: float,
                 fbs: float,
                 glc_3_auc: float,
                 glc_plasma_auc: float,
                 glc_css: float):
        self.__height = height
        self.__bw = bw
        self.__fbs = fbs
        self.__glc_3_auc = glc_3_auc
        self.__glc_plasma_auc = glc_plasma_auc
        self.__glc_css = glc_css
        self.__relative_bw = 0 #相対体重の初期値はゼロ
    
    def load_height(self)->float:
        return self.__height
    
    def load_bw(self)->float:
        return self.__bw
    
    def load_fbs(self)->float:
        return self.__fbs
    
    def load_glc_3_auc(self)->float:
        return self.__glc_3_auc
    
    def load_glc_plasma_auc(self)->float:
        return self.__glc_plasma_auc
    
    def load_glc_css(self)->float:
        return self.__glc_css
    
    #相対体重を追加登録する
    def update_rlative_bw(self,relative_bw: float):
        self.__relative_bw = relative_bw
    
    def load_rlative_bw(self)->float:
        return self.__relative_bw