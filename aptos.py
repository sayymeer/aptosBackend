from datetime import date
from dotenv import load_dotenv
import os

from aptos_sdk.account import Account
from aptos_sdk.async_client import RestClient
from aptos_sdk.transactions import TransactionPayload,EntryFunction,TransactionArgument
from aptos_sdk.bcs import Serializer

load_dotenv()

NODE_URL = os.getenv("APTOS_NODE_URL")
PRIV_KEY = os.getenv("ACC_PRIV_KEY")

rest_client = RestClient(NODE_URL)
account = Account.load_key(PRIV_KEY)


async def autoCall():
    '''this function run 2 bcs transactions'''
    trans_arg_1 = [TransactionArgument(date.today().day,Serializer.u64)]
    payload1 = TransactionPayload(EntryFunction.natural(
        f'{account.account_address}::SUCC',
        "getbuylist",
        [],
        trans_arg_1
    ))
    payload2 = TransactionPayload(EntryFunction.natural(
        f'{account.account_address}::SUCC',
        'changeJ',
        [],
        []
    ))
    sign_trans_1 = await rest_client.create_bcs_signed_transaction(account,payload1)
    await rest_client.submit_bcs_transaction(sign_trans_1)
    sign_trans_2 = await rest_client.create_bcs_signed_transaction(account,payload2)
    await rest_client.submit_bcs_transaction(sign_trans_2)
    return

async def RiskData(module:str,func:str):
    '''this function returns data for risk calculation'''
    res = await rest_client.account_resource(account.account_address,f"{account.account_address}::{module}::{func}")
    return res.data