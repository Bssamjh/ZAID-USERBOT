from os import getenv

API_ID = int(getenv("API_ID", "25132383")) #optional
API_HASH = getenv("API_HASH", "78f258fcc057113beec90a803715425a") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6184135499").split()))
OWNER_ID = int(getenv("OWNER_ID", "6184135499")) #ur id
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://BS:<password>@cluster0.hjawjqk.mongodb.net/?retryWrites=true&w=majority") # an database
BOT_TOKEN = getenv("BOT_TOKEN", "5939879014:AAHSgKWNhmkY29e-1aFjYjlEsGbd3t-9wsE")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT") #optional
PM_LOGGER = getenv("PM_LOGGER") # i'd if uh want 
LOG_GROUP = getenv("LOG_GROUP") #id if uh want enable tagaiert
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BABiMZkAUornRZcJ3Y1sAHeJNewfQYRFF_QN63uQc15EXWEqPtKFODupYnU781DNQNUe0Gki9UR3dG-xq7x0JPGfvipCVraKlKkZpYuxK_IoLRHa9avARj03x0X8naIOERZNtsZ0S7evJRHIOxrH6j54qKn_YsyazVCfyTrf_qywx6iLtP-X7XtJpMzfCeNR6B-FUNLnlh2QtBUwbLqzJmvHMuny7FLPwI_4BpFDhBdbQoMZkYTO92bI9rjO4hai-Ll4dXQIgD_0ykRUtldBKrOKWjqLPYM_4Ek28XnLy_bfuFKI6CSl1Y26MDPqdyok2C9nB6D0I0tYgeIX102LXJeXibZ7nQAAAAFwmmtLAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
