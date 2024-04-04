from fastapi import FastAPI,status
from pydantic import BaseModel
from typing import Optional
from fastapi.params import Body

app=FastAPI()
class product(BaseModel):
    product_name:str
    product_price:int
    product_category:str
    product_discount:Optional[int]=0
    product_image:str="https://in.images.search.yahoo.com/search/images;_ylt=Awr1TpJX6gpm3IceAgy7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=no+image&fr2=piv-web&type=E210IN885G0&fr=mcafee#id=8&iurl=https%3A%2F%2Fwww.allianceplast.com%2Fwp-content%2Fuploads%2Fno-image-1024x1024.png&action=click"
p=[{
    "product":"vivo_v23",
    "price":30000,
    "catagire":"mobiles"
    },{
        "product":"asus",

        "price":42000,
        "catagiri":"laptops"
    },{"product":"oppo",
    "price":19000,
    "caatogiri":"mobailes"}
]
@app.get('/products')
def all_products():
    return p
