print("Initializing key generation...")
import requests
import json
import time

baseurl = "https://discord.com/billing/partner-promotions/1180231712274387115/"

payload = "{\"partnerUserId\":\"d5bcb917858985fadb511d725df39e4196d3c45c6530912aa7d60cab2aafcf2a\"}"

headers = {
    'authority': "api.discord.gx.games",
    'accept': "*/*",
    'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
    'content-type': "application/json",
    'origin': "https://www.opera.com",
    'referer': "https://www.opera.com/",
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': "empty",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "cross-site",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
    }
print("Loading 5 keys.")
for i in range(5):
    send = requests.post("https://api.discord.gx.games/v1/direct-fulfillment", data=payload, headers=headers)
    token = json.loads(send.text)["token"]

    print(f"{baseurl}{token}\r\n")
    time.sleep(1)
input("Press Enter to exit...")
