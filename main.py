from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aptos import autoCall,RiskData,placeOrder,PlaceOrderBody
from market import GetRiskStats

scheduler = AsyncIOScheduler()
scheduler.add_job(autoCall,'cron',hour=23,minute=59)
scheduler.start()

app = FastAPI()
app.add_middleware(CORSMiddleware,allow_origins='*')
data = []


async def UpdateData():
    global data
    data = await RiskData()

@app.get('/')
async def root():
    await autoCall()
    return "success"


@app.get('/riskStat')
async def riskStat():
    """This will Give you the Risk"""
    return GetRiskStats(list(map(int,data)))


@app.get('/update')
async def update():
    """This will Update Data"""
    await UpdateData()
    return {'data':data}

@app.get('/view')
async def view():
    """To View Data"""
    return {'data':data}

@app.post('/placeOrder')
async def placeOrderHandler(plc:PlaceOrderBody):
    """To Place Order"""
    await placeOrder(plc)
    return "success"


if __name__ == '__main__':
    uvicorn.run("main:app",port=8000,reload=True)
