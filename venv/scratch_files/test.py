
import json
from blizzardapi import BlizzardApi
from dotenv import dotenv_values


def getWowAchievementCategoriesIndex(clientId, clientSecret):
    apiClient = BlizzardApi(client_id=clientId, client_secret=clientSecret)
    categories = apiClient.wow.game_data.get_achievement_categories_index(region="us", locale="en_US")
    rawJson = json.dumps(categories, indent=4)
    with open("venv/raw_jsons/wowAchievementCategoriesIndex.json", "w") as outfile:
        outfile.write(rawJson)

def getWowAchievementCategory(clientId, clientSecret, categoryId):
    apiClient = BlizzardApi(client_id=clientId, client_secret=clientSecret)
    categories = apiClient.wow.game_data.get_achievement_category(region="us", locale="en_US", achievement_category_id=categoryId)
    rawJson = json.dumps(categories, indent=4)
    with open("venv/raw_jsons/wowAchievementCategories%s.json" % categoryId, "w") as outfile:
        outfile.write(rawJson)

def getWowAchievementIndex(clientId, clientSecret):
    apiClient = BlizzardApi(client_id=clientId, client_secret=clientSecret)
    categories = apiClient.wow.game_data.get_achievements_index(region="us", locale="en_US")
    rawJson = json.dumps(categories, indent=4)
    with open("venv/raw_jsons/wowAchievementIndex.json", "w") as outfile:
        outfile.write(rawJson)

config = dotenv_values("venv/config/.env")
clientId = config["CLIENT_ID"]
clientSecret = config["CLIENT_SECRET"]

getWowAchievementCategoriesIndex(clientId, clientSecret)
getWowAchievementCategory(clientId, clientSecret, categoryId=14922)
getWowAchievementIndex(clientId, clientSecret)
print("Request success!")