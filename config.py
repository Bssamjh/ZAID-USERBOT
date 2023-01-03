from os import getenv

API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5897361894").split()))
OWNER_ID = int(getenv("OWNER_ID", "5897361894")) #ur id
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://BS:<password>@cluster0.hjawjqk.mongodb.net/?retryWrites=true&w=majority") # an database
BOT_TOKEN = getenv("BOT_TOKEN", "5698431322:AAHsfw3tW0zCAlULMxwmrYT5RRGYF2u6puU")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT") #optional
PM_LOGGER = getenv("PM_LOGGER") # i'd if uh want 
LOG_GROUP = getenv("LOG_GROUP") #id if uh want enable tagaiert
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkAuwrf9LilbxNJ4Arm5pfQFfNIWr7eB22wA7ajby7qLVWJ33jiwz0Oz34Kb1HXSdviurVwyY4yVjyQNwxWiJ2DkIEHZ7I0sATJCz1uB-HFEmguVaYqJ7nqc3OorIfGxYn3DGOvcxU1FJT7EKiOnV_XzcmKyh1ARVjh13ZRVein6uB9P_bkS9PJjRLsjMixplu0rz3Q1Mv21KWgHX-Bhpx7Uxpm45vQjF_O4eTdZUvvpYX2CfbYYiLfOckmTWY9OJycIESYgDfnK_OVyWS0b6sFmNgkH9ZnXZrf7Mkasc19VviKif5odN8NjfNlKpRjKX3i7maIwpC2H-cjDc7rXhij9wAAAAFfgpnmAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
