#import設定
import sys
sys.path.append("../src")

from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

#predict_dm_1のテスト
def test_predict_dm_1():
    respose = client.post("/predict/",
                          json={
                                "height": 150,
                                "bw": 50,
                                "fbs": 112,
                                "glc_3_auc": 500,
                                "glc_plasma_auc": 392,
                                "glc_css": 253
                                }
                          )
    assert respose.status_code == 200