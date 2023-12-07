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
MOD_NAME = os.getenv("MOD_NAME")
EXP_ORD_FUNC = os.getenv("EXP_ORD_FUNC")
CHANGE_J_FUNC = os.getenv("CHANGE_J_FUNC")
MARKET_PRICE_FUNC = os.getenv("MARKET_PRICE_FUNC")
PLACE_ORDER_FUNC = os.getenv("PLACE_ORDER_FUNC")


rest_client = RestClient(NODE_URL)
account = Account.load_key(PRIV_KEY)


async def autoCall():
    '''this function run 2 bcs transactions'''
    trans_arg_1 = [TransactionArgument(date.today().day,Serializer.u64)]
    payload1 = TransactionPayload(EntryFunction.natural(
        f'{str(account.account_address)}::{MOD_NAME}',
        f"{EXP_ORD_FUNC}",
        [],
        trans_arg_1
    ))
    payload2 = TransactionPayload(EntryFunction.natural(
        f'{str(account.account_address)}::{MOD_NAME}',
        f'{CHANGE_J_FUNC}',
        [],
        []
    ))
    sign_trans_1 = await rest_client.create_bcs_signed_transaction(account,payload1)
    await rest_client.submit_bcs_transaction(sign_trans_1)
    sign_trans_2 = await rest_client.create_bcs_signed_transaction(account,payload2)
    await rest_client.submit_bcs_transaction(sign_trans_2)
    return

async def RiskData():
    '''this function returns data for risk calculation'''
    res = await rest_client.account_resource(account.account_address,f"{account.account_address}::{MOD_NAME}::{MARKET_PRICE_FUNC}")
    return res['data']['data']


async def placeOrder(privKey:str,amount:int,price:int,timestamp:int,date:int,side:bool,leverage:int):
    account = Account.load_key(privKey)
    trans_arg = [TransactionArgument(amount,Serializer.u64),TransactionArgument(price,Serializer.u64),TransactionArgument(timestamp,Serializer.u64),TransactionArgument(date,Serializer.u64),TransactionArgument(side,Serializer.bool),TransactionArgument(leverage,Serializer.u64)]
    payload = TransactionPayload(
        EntryFunction.natural(
            f'{str(account.account_address)}::{MOD_NAME}',
            f"{PLACE_ORDER_FUNC}",
            [],
            trans_arg
        )
    )
    sign_trans = await rest_client.create_bcs_signed_transaction(account,payload)
    await rest_client.submit_bcs_transaction(sign_trans)
    return