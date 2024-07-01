import uuid
from sqlalchemy import Boolean, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType, EmailType
from datetime import datetime
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUIDType, primary_key=True, index=True, default=uuid.uuid4)
    email = Column(EmailType, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,onupdate=datetime.utcnow)

    profile = relationship("Profile", uselist=False, back_populates="user")


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(UUIDType, primary_key=True, index=True, default=uuid.uuid4)
    bio = Column(String)
    first_name = Column(String(100))
    last_name = Column(String(100))
    profile_pic = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,onupdate=datetime.utcnow)

    user_id = Column(UUIDType, ForeignKey("users.id"))
    user = relationship("User", back_populates="profile")
