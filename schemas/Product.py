from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[int]
    title: str 
    price: int
    description: str
    category: str
    image: str