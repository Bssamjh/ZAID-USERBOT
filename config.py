from os import getenv

API_ID = int(getenv("API_ID", "22961833")) #optional
API_HASH = getenv("API_HASH", "71419fa7321d55b8ee311bc0c01c9abc") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6115381327").split()))
OWNER_ID = int(getenv("OWNER_ID", "6115381327")) #ur id
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://BS:<password>@cluster0.hjawjqk.mongodb.net/?retryWrites=true&w=majority") # an database
BOT_TOKEN = getenv("BOT_TOKEN", "6297956070:AAHsJka3o5br7ZVi58JEiq6NLGi4nwZ-BxQ")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT") #optional
PM_LOGGER = getenv("PM_LOGGER") # i'd if uh want 
LOG_GROUP = getenv("LOG_GROUP") #id if uh want enable tagaiert
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkAqqHKk18h15ZSvxBm-MqN4NoJWwkyp2La6fgD2Hsq4zGXcKoLd-OPqFgA51JBYjV_AqHLobCH-fJAnfgvuHc_-5QgFQPTpjDPrCXPGlc-DJr8GXotARL46G0blEmHLbCOrSvm3OTBBIGIBTGAcRKJX6GC0mL0hTxRAr5dUj5gfU_S7-8ZfCjxxIi12UE_XiGn1BKRQRQBBRDM1KjZzdsT8pi3p_0OvZ7h_GGs_0qziow5CQ7v8Z5M6bvEStABgcCyV7TgHszRhLxJfDvuHVuwXO9jIHJEfvcG3UiEp-jNO5f3CAaRnUfUqkbwZ37fhKzpVAwph-SGLNJnFcdVlGGimgAAAAFsgVBPAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
