# BinanceBatchTransfer

## Introduction:

This project is to transfer token to multiple address in once , you can define the token value between the number to prevent witch attack

## How to use:

1. You need to download these code
2. Create two file :
    1. address.txt : Use to contain address you want to send
        
        How to put the address in the TXT:
        
        ```jsx
        0xefdsafdsf21312312321313...
        0x123123123213jeodsafjlsakdflsdaf...
        0xfesadfedf23e12321edsafasdfsgg
        ....
        .....and so on 
        ```
        
    2. key.json : put the api key you have set up to transfer token
        
        Notice: Make Sure you have setup this API with your IP that you are using now
        
        How to put the API in the JSON file:
        
        ```jsx
        {
            "API_KEY":"Your API key",
            "API_SECRET":"Your Secret key"
        }
        ```
        
3. How to Start?
    1. Make sure you have edited `[main.py](http://main.py)` , you will need to set the amount of the token
