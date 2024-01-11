
import json
from blizzardapi import BlizzardApi
from dotenv import dotenv_values


def getWowCategories(clientId, clientSecret):
    apiClient = BlizzardApi(client_id=clientId, client_secret=clientSecret)
    categories = apiClient.wow.game_data.get_achievement_categories_index(region="us", locale="en_US")
    rawJson = json.dumps(categories, indent=4)
    with open("wowCategories.json", "w") as outfile:
        outfile.write(rawJson)


config = dotenv_values("venv/config/.env")
clientId = config["CLIENT_ID"]
clientSecret = config["CLIENT_SECRET"]

getWowCategories(clientId, clientSecret)
<<<<<<< HEAD
print("Request successful!")
=======
print("Request success!")
>>>>>>> baaa7e9362a97c4b89e5724f6b92e04f0fdfce6a
