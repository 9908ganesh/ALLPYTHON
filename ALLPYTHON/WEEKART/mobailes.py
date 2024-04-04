from fastapi import FastAPI,status
from pydantic import BaseModel
mob=FastAPI()
class m_new(BaseModel):
    phnm:str
    price:int
    feautures:str
    MadeIn:str
    category:str

m=[
    {
        "phnm":"vivoz1pro",
        "price":16000,
        "feautures":"4GBRAM,64ROM",
        "MadeIN":"chaina",
        "category":"mobiles"
    },{
        "phnm":"VIVO_V235G",
        "price":29999,
        "feautures":"8GBRAM,128ROM",
        "MadeIN":"chaina",
        "category":"mobiles"        
    },{
        "phnm":"SAMSANG",
        "price":18000,
        "feautures":"6GBRAM,64ROM",
        "MadeIN":"INDIA",
        "category":"mobiles"
    },{
        "phnm":"OPPO",
        "price":19000,
        "feautures":"6GBRAM,128ROM",
        "MadeIN":"chaina",
        "category":"mobiles"
    },{
        "phnm":"ONEPLUS",
        "price":36000,
        "feautures":"12GBRAM,512ROM",
        "MadeIN":"UAS",
        "category":"mobiles"
    }
]
@mob.get('/')
def get_All_Moba_iles():
    return m
@mob.post('/mobaile_new',status_code=status.HTTP_201_CREATED)
def get_newmobile(newm:m_new):
    mobaile=newm.model_dump()
    m.append(mobaile)
    print(mobaile)
    return{'data':mobaile}