import bcrypt

class Security_modules:
    #パスワードのハッシュ化
    @staticmethod
    def hash_value(value)->str:
        return bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    #パスワードの認証
    @staticmethod
    def check_password(plain_password :str, hashed_password :str)->bool:
        
        if hashed_password == None:
            return False
        
        return bcrypt.checkpw(plain_password.encode('utf-8'), bytes(hashed_password,'utf-8'))