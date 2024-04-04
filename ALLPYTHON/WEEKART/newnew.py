from fastapi import FastAPI,status
from pydantic import BaseModel
from typing import Optional



application=FastAPI()
class newpost(BaseModel):
    product:str
    price:int
    quantity:str
    category:str
    offer:Optional[str]=None

products=[{
        'product':'colgate',
        'price':'69',
        'quantity':'250g',
        'category':'past',
        'offer':'buy 3 get 1 free'
    },{
        'product':'santoor',
        'price':'39',
        'quantity':'100g',
        'category':'face soap',
        'offer':'buy 4 get 1 free'
    },{
        'product':'FairAndHandsome',
        'price':'189',
        'quantity':'150g',
        'category':'MensFaceCream',
        'offer':'buy 5 get 1 free'        
    },{
        'product':'AtaPowder',
        'price':'369',
        'quantity':'10kg',
        'category':'Food',
        'offer':'buy 3 get 1 free'
    }
    ]
@application.get('/')
def get_products():
    return products
@application.post('/create',status_code=status.HTTP_201_CREATED)
def posted_post(new_post:newpost):
    new__post=new_post.model_dump()
    new__post['id']=156
    products.append(new__post)
    return {'data':new__post}
