#データベース関連の設定
from sqlalchemy import create_engine
import os

#環境変数化
url = os.environ['MYSQL_URL']
engin = create_engine(url)

