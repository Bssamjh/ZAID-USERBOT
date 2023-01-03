from os import getenv

API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5972069235").split()))
OWNER_ID = int(getenv("OWNER_ID", "5972069235")) #ur id
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://BS:<password>@cluster0.hjawjqk.mongodb.net/?retryWrites=true&w=majority") # an database
BOT_TOKEN = getenv("BOT_TOKEN", "5779669372:AAHK9gxynRF5vFZKB35J5sQeZeZRftMhmXo")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT") #optional
PM_LOGGER = getenv("PM_LOGGER") # i'd if uh want 
LOG_GROUP = getenv("LOG_GROUP") #id if uh want enable tagaiert
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkAc93QoM8NfJqpom0iLl6F0O8KZ7_I6b9l9G2N-_WYjkY2m2_y28C1VLLPLnxHzNXqUo3kUk3PYPciTS4Z3cCZfan6s-QB3xw5Q2u91PEyfGiasbHyD1WysUwjKApZuPOStuPSTwKXoObEnJJp-h51vHj4w0by_4QjOsgddrGyxaV6S6rQIo9G-I__kDdjwVCmLoQwFybYwW3ECVrPOTQieuQYoyL6A955O5A7RyFxScyLMCIB2kfnoNygVlLqjkSOw6LgZcspgKP_-XnUhgVESmvmXidb3WU6RxOkA2_DVd5714ZJKUpJMr8kax8U4DlSvd2SqbRMI3CENsFEafkmGwAAAAFj9otzAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
