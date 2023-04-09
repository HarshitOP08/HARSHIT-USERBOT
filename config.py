import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "26807432")) #optional
API_HASH = getenv("API_HASH", "8c7b78e307000301d0e1a17157076696") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5656982887").split()))
OWNER_ID = int(getenv("OWNER_ID", "6072499456"))
MONGO_URL = getenv("mongodb+srv://Spambot69:<password>@cluster0.r06ipmt.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6048067676:AAEpIieamQ6clJVaolGPr1rNZo977raDGx0")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAILdyTaLxzODkJO_gdRQmHl5krvdKAyPtMV6TDoUS-O5nGqBb2173Sp03VNWiiejTwIdlgZj-5AlLjkEH-3ffP5vWC41IMJoihJlHmhYUHZckNO7XP6gqgeotHFIDL07nlHL2ulwljoin73Dxbp1RT50uMKIRMrM7YUdJiPoPdXqZGYLs7levJHIEoyxE9_Q_igji8AyzPInYc4NmCoX8Q0WT46NQJQmCCmKWTHzRDIYVuwR-XW6ZMQVUjAztBJoiYDVC-7WMinaMXCSLcs9emHpeGSWLgsye47ESdjO3KYZgZ68-CPF9puBhnhecwgiQ-F9t47YZMlPyB5ZJupEBsAAAAAFp8v0AAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
