# backend/app/schemas.py
from typing import List, Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class ClothingItemBase(BaseModel):
    image_url: str
    type: str
    color: str
    season: str
    tags: str
    user_id: int

class ClothingItemCreate(ClothingItemBase):
    pass

class ClothingItem(ClothingItemBase):
    id: int
    class Config:
        orm_mode = True

class OutfitBase(BaseModel):
    name: Optional[str] = None
    occasion: str
    clothing_item_ids: List[int]
    user_id: int

class OutfitCreate(OutfitBase):
    pass

class Outfit(OutfitBase):
    id: int
    clothing_items: List[ClothingItem]
    class Config:
        orm_mode = True
