from fastapi.testclient import TestClient
from main import app,Body

client = TestClient(app)

#predict_dm_1のテスト
def test_predict_dm_1():
    respose = client.post("/predict/",
                          json={
                                "bw": 1.07,
                                "fbs": 112,
                                "glc_3_auc": 500,
                                "glc_plasma_auc": 392,
                                "glc_css": 253
                                }
                          )
    assert respose.status_code == 200