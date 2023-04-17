from typing import Optional
from pydantic import BaseModel

class Users(BaseModel):
    name: Optional[str]
    email: str
    last_name: Optional[str]
    username: Optional[str]
    identification: Optional[str]
    password: str
    