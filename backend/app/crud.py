# backend/app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas

# User CRUD
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Clothing CRUD
def create_clothing_item(db: Session, image_url, type, color, season, tags, user_id):
    item = models.ClothingItem(
        image_url=image_url,
        type=type,
        color=color,
        season=season,
        tags=tags,
        user_id=user_id
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_user_clothing(db: Session, user_id: int):
    return db.query(models.ClothingItem).filter(models.ClothingItem.user_id == user_id).all()

# Outfit CRUD
def save_outfit(db: Session, outfit_data: schemas.OutfitCreate):
    items = db.query(models.ClothingItem).filter(models.ClothingItem.id.in_(outfit_data.clothing_item_ids)).all()
    outfit = models.Outfit(
        name=outfit_data.name,
        occasion=outfit_data.occasion,
        user_id=outfit_data.user_id,
        clothing_items=items
    )
    db.add(outfit)
    db.commit()
    db.refresh(outfit)
    return outfit

def get_user_outfits(db: Session, user_id: int):
    return db.query(models.Outfit).filter(models.Outfit.user_id == user_id).all()

