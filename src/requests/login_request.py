from pydantic import BaseModel

class Login_request(BaseModel):
  user_name: str
  password: str
