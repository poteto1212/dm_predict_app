import pandas as pd
import bcrypt
import sys
sys.path.append("../src")
import settings

df=pd.read_csv("/src/seeds/datasets/users_seed.csv")
print(df)

#ハッシュ化対象カラム
column_to_hash = 'password'
print(column_to_hash)

def hash_value(value)->str:
    return bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# 対象列をハッシュ化して更新
df[column_to_hash] = df[column_to_hash].apply(hash_value)

print(df)

engin = settings.engin
#データベースへの流し込み処理
df.to_sql("users",engin,if_exists="append",index=False)


