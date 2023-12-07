# Starting server

```env
APTOS_NODE_URL="https://fullnode.devnet.aptoslabs.com/v1"
ACC_PRIV_KEY="yourprivkey"
MOD_NAME="Coin1"
EXP_ORD_FUNC="expiryOrderBookNotMatch"
CHANGE_J_FUNC="changeJ"
MARKET_PRICE_FUNC="MarketPriceList"
PLACE_ORDER_FUNC="place_Order"
```

Create `.env` file like above and then run the below code to start server.

```bash
pip3 install -r requirement.txt
python3 main.py
```

Your sever will start on `localhost:8000` by default.

## Documentation

You can visit `localhost:8000/docs` to view API docs.
