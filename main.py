from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aptos import autoCall,RiskData,placeOrder
from market import GetRiskStats
from pydantic import BaseModel

scheduler = AsyncIOScheduler()
scheduler.add_job(autoCall,'cron',hour=23,minute=59)
scheduler.start()

app = FastAPI()
app.add_middleware(CORSMiddleware,allow_origins='*')

data = []

class PlaceOrderBody(BaseModel):
    privKey:str
    amount:int
    price:int
    timestamp:int
    date:int
    side:bool
    leverage:int

async def UpdateData():
    global data
    data = await RiskData()

@app.get('/')
async def root():
    await autoCall()
    return "success"


@app.get('/riskStat')
async def riskStat():
    return GetRiskStats(list(map(int,data)))


@app.get('/update')
async def marketprice():
    await UpdateData()
    return {'data':data}

@app.get('/view')
async def view():
    return {'data':data}

@app.post('/placeOrder')
async def placeOrderHandler(plc:PlaceOrderBody):
    await placeOrder(plc.privKey,plc.amount,plc.price,plc.timestamp,plc.date,plc.side,plc.leverage)
    return "success"


if __name__ == '__main__':
    uvicorn.run("main:app",port=8000,reload=True)
