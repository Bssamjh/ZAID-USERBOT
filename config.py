from os import getenv

API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5845537042").split()))
OWNER_ID = int(getenv("OWNER_ID", "5845537042")) #ur id
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://BS:<password>@cluster0.hjawjqk.mongodb.net/?retryWrites=true&w=majority") # an database
BOT_TOKEN = getenv("BOT_TOKEN", "5843455354:AAFRp-I_AzDYZfsIgTgwVnrZwMqjegHSZqk")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT") #optional
PM_LOGGER = getenv("PM_LOGGER") # i'd if uh want 
LOG_GROUP = getenv("LOG_GROUP") #id if uh want enable tagaiert
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkAjY9fWZx14MUuO2F6-77Fnk6jAtG5sNny6r2QqHgjf4pGaV4gxfGSccv2R7iiFcVTEakUOWPV0X9yUta5aOjDVgAcRDQ160srs-5O5Ira5gJCSXNseUA_5yMH6rDMXwkc4o1xRYD4G1FhsvjcNI0N31E5xHQf5E43M9eLq5AQR8rdNXFKYOlOJ_s-VB_rw1oYggdWs3ZEpKeOBx24o_1J_ES8X2fyFoP7UjBhMYK5k4T8msi0lWcOMba1Df-TxiWb6-ckyKBTs-yDNmdNxqHO73jGo7oM9XFEXcO8IDWL1lKe_CvBMfaLGaYs67OvotGaLYHj-xJ8H-rnyhuc7tDmzgAAAAFca9ESAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
