from sqlalchemy import Column, Integer, String,CheckConstraint
from sqlalchemy.orm import relationship
from .base_model import Base
from .admin_model import Admin_model#リレーションテーブルも明示しておく必要がある

class User_model(Base):
    __tablename__ = "users"
    id = Column(
        Integer, 
        primary_key=True, 
        index=True
        )
    nickname = Column(
        String(length=15)
        )
    user_name = Column(
        String(length=30), 
        unique=True, 
        index=True
        )
    password = Column(
        String(length=70)#bcryptは60文字のハッシュを生成　
        )
    security_ask = Column(
        Integer,
        CheckConstraint('security_ask >= 1 AND security_ask <= 5')
        )
    security_ask_answer = Column(
        String(length=20)
        )
    graduate = Column(
        Integer
        )
    level = Column(
        Integer,
        CheckConstraint('level >= 1')
        )
    admin = relationship("Admin_model", back_populates="user")