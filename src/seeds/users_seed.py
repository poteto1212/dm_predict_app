import pandas as pd
import bcrypt
import sys
sys.path.append("../src")
import settings

df=pd.read_csv("/src/seeds/datasets/users_seed.csv")
print(df)

#ハッシュ化対象カラム
column_to_hash = 'password'

#TODO モジュール化
def hash_value(value)->str:
    return bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

df[column_to_hash] = df[column_to_hash].apply(hash_value)
engin = settings.engin
df.to_sql("users",engin,if_exists="append",index=False)


