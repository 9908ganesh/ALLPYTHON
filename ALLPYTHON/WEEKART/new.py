from fastapi import FastAPI,status
from typing import Optional
from pydantic import BaseModel
from random import randrange



web=FastAPI()
class newproduct(BaseModel):
    pro_name:str
    pro_price:int
    pro_category:str
    discount:Optional[int] = None
pro=[
        {
            'pname':'carrier',
            'price':45000,
            'category':'air conditionars',
            'image_url':"https://in.images.search.yahoo.com/search/images;_ylt=AwrKGBrsqgtmoeoKO8i7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=no+image&fr2=piv-web&type=E210IN885G0&fr=mcaf",
            'discount':'10%'
            
            
        },{
            'pname':'koollife',
            'price':500,
            'category':'fans',
            'image_url':"https://in.images.search.yahoo.com/search/images;_ylt=AwrKGBrsqgtmoeoKO8i7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=no+image&fr2=piv-web&type=E210IN885G0&fr=mcaf",
            'discount':'12%'
        },{
            'pname':'bhagavan',
            'price':59,
            'category':'notebook',
            'image_url':"https://in.images.search.yahoo.com/search/images;_ylt=AwrKGBrsqgtmoeoKO8i7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=no+image&fr2=piv-web&type=E210IN885G0&fr=mcaf",
            'discount':'05%' 
        },{
            'pname':'realme',
            'price':1500,
            'category':'headphons',
            'image_url':"https://in.images.search.yahoo.com/search/images;_ylt=AwrKGBrsqgtmoeoKO8i7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=no+image&fr2=piv-web&type=E210IN885G0&fr=mcaf",
            'discount':'9%'
        },{
            'pname':'lenova',
            'price':42500,
            'category':'laptos',
            'image_url':"https://in.images.search.yahoo.com/search/images;_ylt=AwrKGBrsqgtmoeoKO8i7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=no+image&fr2=piv-web&type=E210IN885G0&fr=mcaf",
            'discount':'07%'
        }
    ]

@web.get('/')
def get_products():
    return pro

@web.post('/test/create', status_code=status.HTTP_201_CREATED)
def create_post(new_item: newproduct):
    a=new_item.model_dump()
    a['id']=randrange(1,900)
    pro.append(a)
    return{'data':a}

@web.get('/test/create/2')
def get_latest_pro():
    return pro[slice(len(pro)-5,len(pro)-1)]


