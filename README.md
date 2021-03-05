# Code to use bot telegram with docker


This bot sends messages every 5 minutes to a telegram chat with cryptocurrency information, specifically Bitcoin and Ethereum (It can be configured)

Requirements :

 - You need an api key from coinmarketcap.com and place it in the config.json file
 - Create a telegram bot with BotFather https://core.telegram.org/bots (get bot ID)

Go to:

https://www.docker.com/get-started

Download app docker and run it

After that

`git clone https://github.com/anthonyperniah/BotTelegramWithDocker.git`  

and then, enter in this folder:

 - Modify the config.json with your data 
				 - id_bot
				 - api_key_cmc
				 - chat_id
				 - time_to_send
		
 - Modify the python file `(bot_crypto.py)` if you require

and now in the Terminal

Build Image:

 - `docker build -t bot_telegram `

Create Container with this image:

 - `docker run --name bot_telegram_app -d bot_telegram`


> **Note:** This bot was made with a focus on simplicity