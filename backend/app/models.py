# backend/app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

# Many-to-many: outfit <-> clothing items
outfit_clothing_table = Table(
    'outfit_clothing',
    Base.metadata,
    Column('outfit_id', Integer, ForeignKey('outfits.id')),
    Column('clothing_item_id', Integer, ForeignKey('clothing_items.id')),
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)

    clothing = relationship("ClothingItem", back_populates="owner")
    outfits = relationship("Outfit", back_populates="owner")

class ClothingItem(Base):
    __tablename__ = "clothing_items"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    type = Column(String)
    color = Column(String)
    season = Column(String)
    tags = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="clothing")
    outfits = relationship("Outfit", secondary=outfit_clothing_table, back_populates="clothing_items")

class Outfit(Base):
    __tablename__ = "outfits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    occasion = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="outfits")
    clothing_items = relationship("ClothingItem", secondary=outfit_clothing_table, back_populates="outfits")
