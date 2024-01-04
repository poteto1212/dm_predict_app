class Predict_dm_1_dto:
    def __init__(self,
                 bw: float,
                 fbs: float,
                 glc_3_auc: float,
                 glc_plasma_auc: float,
                 glc_css: float):
        self.__bw = bw
        self.__fbs = fbs
        self.__glc_3_auc = glc_3_auc
        self.__glc_plasma_auc = glc_plasma_auc
        self.__glc_css = glc_css
    
    def load_bw(self):
        return self.__bw
    
    def load_fbs(self):
        return self.__fbs
    
    def load_glc_3_auc(self):
        return self.__glc_3_auc
    
    def load_glc_plasma_auc(self):
        return self.__glc_plasma_auc
    
    def load_glc_css(self):
        return self.__glc_css