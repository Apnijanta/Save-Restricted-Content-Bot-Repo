# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25912801"))
API_HASH = getenv("API_HASH", "f14e8717578935103e2774559184a345")
BOT_TOKEN = getenv("BOT_TOKEN", "6728704718:AAHbgt-igQ0pfqderXjQtG2IdYNPQw-Wj7I")
OWNER_ID = int(getenv("OWNER_ID", "1306706536"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://pranchal1419:<password>@cluster0.gicdshq.mongodb.net/")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002198337850"))
SESSION = getenv("PYROGRAM_V2_SESSION", "BQAANhXGEH3Do8i1LRheDnL2qjKxoeglsVIEsaXKIqs6gFatq1tA2NndbauyNue2Sn0oEo85NM5Ck4odv86vDbjEDGx8lN_c9IZd3W0AOWPO18FG1IRW-hV-lHtkRw6oipQUxrXW6ntGEKLUqIPH43VfspEY4Gv7Eg5EG29hfFcLtRU4BAm7SEoc6x09ZOMcLeHdCftpv5_5TndVffUQAXKPHDBZmNZ8oGEopPt6v4ZTDjO0LnJcadGpB254qpu4Q-bM76QstCtyS4ON5yWYdDwQQS_YldHakO2RPAdKrz5IZ5-u8QWOXao74HQsnfsfXcN-kkTtPv3RcrUUTQtBGvy0TeLCaAA")
FORCESUB = getenv("FORCESUB", "aravsave")
