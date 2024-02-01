import bcrypt

class Security_modules:
    #パスワードのハッシュ化
    @staticmethod
    def hash_value(value)->str:
        return bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    #パスワードの認証
    @staticmethod
    def check_password(plain_password :str, hashed_password :str)->bool:
    # ハッシュ化されたパスワードと平文パスワードの比較
        print(hashed_password)
        return bcrypt.checkpw(plain_password.encode('utf-8'), bytes(hashed_password,'utf-8'))