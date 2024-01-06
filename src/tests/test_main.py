#import設定
import sys
sys.path.append("../src")

from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

#predict_dm_1のテスト
def test_predict_dm_1():
    respose = client.post("/predict_dm_1/",
                          json={
                                "height": 150,
                                "bw": 50,
                                "fbs": 112,
                                "glc_3_auc": 500,
                                "glc_plasma_auc": 392,
                                "glc_css": 253
                                }
                          )
    #正常なレスポンスが帰る
    assert respose.status_code == 200
    
    #レスポンスパラメータ
    predict_val = respose.json()["predict_val"]
    result = respose.json()["result"]
    
    #レスポンスの型が正しい
    assert type(predict_val) == str
    assert type(result) == str
    
    #モデル出力と判定結果が一致している
    light_list = {"0":"糖尿病の可能性は低い","1":"糖尿病の可能性が高い"}
    assert light_list[predict_val] == result