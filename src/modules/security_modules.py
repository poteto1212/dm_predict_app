import bcrypt

class Security_modules:
    @staticmethod
    def hash_value(value)->str:
        return bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')