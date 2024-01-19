import json
from blizzardapi import BlizzardApi


def getWowAchievementCategoriesIndex(clientId, clientSecret):
    apiClient = BlizzardApi(client_id=clientId, client_secret=clientSecret)
    categories = apiClient.wow.game_data.get_achievement_categories_index(region="us", locale="en_US")
    rawJson = json.dumps(categories, indent=4)
    with open("venv/raw_jsons/wowAchievementCategoriesIndex.json", "w") as outfile:
        outfile.write(rawJson)
    return(rawJson)

def getWowAchievementCategory(clientId, clientSecret, categoryId):
    apiClient = BlizzardApi(client_id=clientId, client_secret=clientSecret)
    categories = apiClient.wow.game_data.get_achievement_category(region="us", locale="en_US", achievement_category_id=categoryId)
    rawJson = json.dumps(categories, indent=4)
    with open("venv/raw_jsons/wowAchievementCategories%s.json" % categoryId, "w") as outfile:
        outfile.write(rawJson)
    return(rawJson)

def getWowAchievementIndex(clientId, clientSecret):
    apiClient = BlizzardApi(client_id=clientId, client_secret=clientSecret)
    categories = apiClient.wow.game_data.get_achievements_index(region="us", locale="en_US")
    rawJson = json.dumps(categories, indent=4)
    with open("venv/raw_jsons/wowAchievementIndex.json", "w") as outfile:
        outfile.write(rawJson)
    return(rawJson)

def getWowAchievement(clientId, clientSecret, achievmentId):
    apiClient = BlizzardApi(client_id=clientId, client_secret=clientSecret)
    categories = apiClient.wow.game_data.get_achievement(region="us", locale="en_US", achievement_id=achievmentId)
    rawJson = json.dumps(categories, indent=4)
    with open("venv/raw_jsons/wowAchievement%s.json" % achievmentId, "w") as outfile:
        outfile.write(rawJson)
    return(rawJson)
