from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "18286764"))
API_HASH = getenv("API_HASH", "f88e25386cd833a66d15a08d6bc30351")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN", "5920443941:AAG1UJMR9X7QvM-wUH617Bz8pU-MRqlpM8E")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001740477053"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Lallumic: Lallumic@cluster0.hwfluz1.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1471469091").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/dc3c8d8f04af441dc2e87.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/dc3c8d8f04af441dc2e87.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TAMILCHATS_MAKKAL")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/Alinallmovies")

STRING_SESSION = getenv("STRING_SESSION", "BQEXCKwAXqk4HhKtxCM9Wo6moGonHQEMdG1e5uSZByeNwrPm_HMoQoeCCArFJF4PLbPqp5NPlKNVeaaSHQktG7yAiwGIiH2IqC6Dpeq0teJ7gc9TLGYhVViNW__Nrgj-Y20XCFdwst2XTqYCo_9vFJZ1pooyxA9hciA5in-kXe_OpZi4V5sznsesSh-kN0-As-_AYUmsX6GkTYmDfmpYxA1Xll5eBnQ17R56gteyguRb3f8O8in3Dv-VvBRVyAHioa33BW8-FJlBkJcO7hv5U9VjhT403uWyjkzqc5dBOYcAl8Kz-gEZn4Qcu7alf8_T9GRoWC0weZO0uJ0Bsp-JL2ZPhIXJKQAAAAExDRpeAA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1471469091").split()))
