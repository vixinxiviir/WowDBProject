
import json
import pandas as pd
import requests
from blizzardapi import BlizzardApi
from dotenv import dotenv_values




i = 1
finalTable = pd.DataFrame()
while True:

    url ='https://us.api.blizzard.com/data/wow/search/item?namespace=static-us&name.en_US=&orderby=id&_page=1&&id=[%s,]&_pageSize=1000&access_token=USiPyLgZJdM8BjsDShmlXdkOhfBhagU5D0' % i
    request = requests.get(url=url)
    rawJson = json.dumps(request.json())
    itemPage = pd.read_json(rawJson)
    finalTable = pd.concat([finalTable, itemPage])
    print(len(finalTable))
    try:
        i = itemPage['results'][999]['data']['id']
    except:
        break
finalTable.to_excel('~/Documents/wowApiItem.xlsx')


# url ='https://us.api.blizzard.com/data/wow/search/creature?namespace=static-us&name.en_US=&orderby=id:desc&_page=%s&access_token=USiPyLgZJdM8BjsDShmlXdkOhfBhagU5D0' % i
# request = requests.get(url=url)
# rawJson = json.dumps(request.json())
# creaturePage = pd.read_json(rawJson)


# config = dotenv_values("venv/config/.env")
# clientId = config["CLIENT_ID"]
# clientSecret = config["CLIENT_SECRET"]
# apiClient = BlizzardApi(client_id=clientId, client_secret=clientSecret)
# categories = apiClient.wow.game_data.get_item_set(item_set_id=757, region='us', locale='en_US')
# rawJson = json.dumps(categories, indent=4)
# with open("venv/raw_jsons/wowItemSet757.json", "w") as outfile:
#     outfile.write(rawJson)

print("Request success!")