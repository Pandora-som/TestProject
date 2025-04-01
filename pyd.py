from pydantic import BaseModel, Field

class Item(BaseModel):
    name:str=Field(example='Toster',min_length=2, max_length=100)
    price: float=Field(example='200', gt=0)
    description:str | None=Field(None, example='hot toster', max_length=500)