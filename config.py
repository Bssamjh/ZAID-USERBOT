from os import getenv

API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5572426405").split()))
OWNER_ID = int(getenv("OWNER_ID", "5572426405")) #ur id
MONGO_URL = getenv("MONGO_URL","mongodb+srv://Zaid:Zaid@cluster0.e806k8s.mongodb.net/?retryWrites=true&w=majority") # an database
BOT_TOKEN = getenv("BOT_TOKEN", "5780716702:AAFBlhDMmHQM4YWh4dSzYfKL0cu1IFEaPQM")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT") #optional
PM_LOGGER = getenv("PM_LOGGER") # i'd if uh want 
LOG_GROUP = getenv("LOG_GROUP") #id if uh want to enable tagalert
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "1BJWap1sBuwYNkHXQiawMA5Ekqie0hxaWCrkFGu_FykIGBHSA6_EDn2MKXGTzeTB5MjQ6B7kSNkL7SN7FIJe9tu6lKjxQpHLNXUbftvHHs4_ze_k2Su3AlVE9MCbeG9Oy3efgDnHhiNlpU27fhdpOIXB82_iSmAAexLFEwD7Iww-p80ZX5i1Wqto5119j22lYfHgJd-6qjZuc_IeZn0Cs5nBtCBdtspp8YDytyRhaUPJSSAsSXew9x0HYEViUCvOEG5zyk-oHa_H-wqburB7-Q-FGDzGcJPyrJ_hipDtaiexwFGfepZacqZpPwmDmEpZOIjbAl5L0cqVCkylsYAkhJFHlgzQtii0=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
