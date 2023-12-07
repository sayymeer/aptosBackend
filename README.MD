# Starting server

```env
APTOS_NODE_URL="https://fullnode.devnet.aptoslabs.com/v1"
ACC_PRIV_KEY="0xf603ba08e7ca86fcf30297bb4c4fbc2fc2599f890052f73b16dfbe7e"
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
