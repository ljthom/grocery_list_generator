from sqlalchemy import Column, String, Integer
from pantry.models.base_model import BaseModel


class IngredientEntry(BaseModel):
    __tablename__ = 'ingredients'
    name = Column(
        String(32),
        nullable=False,
        info={'label': 'Ingredient Name'}
    )
    quantity = Column(
        Integer,
        nullable=True,
        info={'label': 'Quantity'}
    )
    unit = Column(
        String(32),
        nullable=True,
        info={'label': 'Unit of Measure'}
    )
