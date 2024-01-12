
import json
from blizzardapi import BlizzardApi
from dotenv import dotenv_values



config = dotenv_values("venv/config/.env")
clientId = config["CLIENT_ID"]
clientSecret = config["CLIENT_SECRET"]
apiClient = BlizzardApi(client_id=clientId, client_secret=clientSecret)
categories = apiClient.wow.game_data.get_realm(region="us", locale="en_US", realm_slug=1182)
rawJson = json.dumps(categories, indent=4)
with open("venv/raw_jsons/wowRealm1182.json", "w") as outfile:
    outfile.write(rawJson)

print("Request success!")