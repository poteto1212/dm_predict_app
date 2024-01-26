from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import Base

#TODO 管理者テーブルを作成する
class Admin_model(Base):
    __tablename__ = "admins"
    id = Column(
        Integer, 
        primary_key=True, 
        index=True
        )
    user_id = Column(
        Integer, 
        ForeignKey('users.id')
        )
    #ユーザーモデルとの1:1リレーションを構築
    user = relationship("User_model", uselist=False,back_populates="admin")