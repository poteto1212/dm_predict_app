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
    category = respose.json()["Category"]
    predict = respose.json()["Preduct"]
    
    #レスポンスの型が正しい
    assert type(category) == str
    assert type(predict) == str
    
    #モデル出力と判定結果が一致している
    light_list = {"0":"糖尿病の可能性は低い","1":"糖尿病の可能性が高い"}
    assert light_list[category] == predict