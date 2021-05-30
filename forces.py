import requests as req
from pprint import pprint

key = "7638781df23f42f99a4311baca9b702b318cb54d"
secret = "8273a85c98569081719e009740e1dbe01d41ee82"

base_url = "https://codeforces.com/api/"
User = "user.info"
payload = {'handles':'coldblow'}

me = req.get(base_url+User,params=payload)

my_data = me.json()['result'][0]

print(my_data['handle'])