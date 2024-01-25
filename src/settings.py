#データベース関連の設定
from sqlalchemy import create_engine

url = "mysql+mysqlconnector://poteto1212:Makt0112pc-49466@mariadb:3306/app-data"
engin = create_engine(url)