from models.Base import Base
# from models.CEO import CEO
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

class CEO(Base):
    __tablename__ = "apple_ceos"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug = Column(String)
    year_served = Column(Integer)
    
class CEOCreate(BaseModel):
        name: str
        slug: str
        year_served: int