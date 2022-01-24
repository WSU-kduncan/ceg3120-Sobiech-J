The following is a guide to set up a Python Discord Bot similar to the one in this folder. A more detailed outline can be found at https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python .

Setup:
-This bot requires an API token. To get one login or create a Discord account on their webpage. From there head to the developer portal, and select the new application button in the top right. You will need to enter a project name and create a bot under the bot tab. This bot will then have a API token that must be copied and put in a file your bot.py script can access. Best practice is to put the token somewhere secure that will not be uploaded to a git repository if you are using git. In that case the token can be saved in a secret .env file in the bot script's directory. If the bot is being developed locally and deployed elsewhere, make sure to copy the .env file and put it with the deployed files.

- If the token is saved in the .env file the bot.py code will need to access the file to get the token. This requires the python-dotenv library. Regardless, this code will require python to run and the discord.py script. The script does not come with the default version of python and must be downloaded. Download through pip is recommended.

- This bot was developed in Ubuntu Server. The default python2 installation did not work well with the libraries mentioned above. It is recommended to install python3 as well as pip3. If you are unable to download discord.py or python-dotenv try installing python3 and pip3 first then use pip3 for the installs.


Usage:
-This bot will output text quotations when certain words are entered into a Discord server that the bot is active in. To get a response a user must enter a certain phrase without @ messaging the bot. Entering the phrase `towel!` (without quotation marks) will cause the bot to output one of various quotes to the server's chat. Using the phrase `Abe!` (again without quotations) will cause the server to post a famous Abraha Lincoln quote to the server's chat.


Research:
-The bot, like any computer program, requires a computer to run on. While one could run this script 24/7 on their home computer, there are better options. Cloud services - if you are willing to pay for them - can run the bot at all times. This is a better solution than a home computer as the cloud will keep the bot running at virtually all times. You can also host the bot yourself on a dedicated server you own. Raspberry Pis are cheap, small computers that are powerful enough to run a Discord bot. I recommend hosting your bot at home with cheap computer like a Raspberry Pi if a Discord bot is the only program you plan to run. With the services the bot is offering setup should be easy and should not require any port forwarding required with other services. Constant internet connection will be required if you decide to host the bot yourself.
