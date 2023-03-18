
# Discord Vanity URL Checker & Changer

This is a Python script that allows you to check if a Discord vanity URL is available and change it if it's not.




## Requirements

- Python 3.x
- colorama
- pymongo
- pystyle
- requests

  
## Demo

1. Clone this repository
2. Install the dependencies listed above: `pip install -r requirements.txt`
3. Run the script: `python vanity.py`
4. Enter your Discord bot token, Discord webhook URL, vanity URL, and the server ID where you want to change the URL. (or use inputs)

The script will check if the vanity URL is available. If it's not, it will change it to the provided URL and send a message to the webhook. If it's available, it will keep trying until it's not.

## Credits

This script was created by **sysx1337**

  
