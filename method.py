import json
from binance.client import Client
from binance.exceptions import BinanceAPIException
import random
import os



now_path = os.getcwd()
with open(now_path+'/key.json') as f:
    keydata = json.load(f)



client = Client(keydata['API_KEY'], keydata['API_SECRET'])










def getHistoryTransfer():
    '''
    Get history transfer from binance
    '''
    deposits = client.get_deposit_history()
    for item in deposits:
        print(item)

def sendToken(address,amount,token,network):
    '''
    arg:
        address : 地址
        amount : 要轉的金額
    
    network:
        MATIC
        BSC
        ARBITRUM
        FTM
        OPTIMISM
        ETH
        TRX
    '''
    try:
        # name parameter will be set to the asset value by the client if not passed
        result = client.withdraw(
                coin=token,
                address=address,
                amount=amount,
                network=network
            )
        print('發送成功 ',address , '金額 :',amount)
    except BinanceAPIException as e:
        print(e)
def random_float(start,end):
    '''
    arg:
        start : start number
        end : end number
    '''
    random_number = random.uniform(start, end)
    return random_number




