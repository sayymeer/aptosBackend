from fastapi import FastAPI
import uvicorn
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aptos import autoCall,RiskData
from market import GetRiskStats

scheduler = AsyncIOScheduler()
scheduler.add_job(autoCall,'cron',hour=23,minute=59)
scheduler.start()

app = FastAPI()

@app.get('/')
async def root():
    await autoCall()
    return "success"


@app.get('/riskStat')
async def riskStat():
    data = await RiskData("Coin1","MarketPrice")
    return GetRiskStats(data)



if __name__ == '__main__':
    uvicorn.run("main:app",port=8000,reload=True)
