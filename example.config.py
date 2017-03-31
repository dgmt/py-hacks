# Paycheck in euros
PAYCHECK = 8000

# Currency Xchange
API_KEY = "<API_key>"
ADDRESS = "http://api.kursna-lista.info/{}/kursna_lista/json".format(API_KEY)

# Mongo
USER = "<username>"
PASS = "<password>"
DB_NAME = "<db_name>"
MONGO_STRING = "mongodb://{}:{}@ds063218.mlab.com:63218/{}".format(
    USER, PASS, DB_NAME)

CURRENCY_MONGO_COLLECTION = "XCH"

# Telegram
TELEGRAM_TOKEN = "<token>"
REPORT_MSG = "Euro is [[eur]], your paycheck is [[paycheck]]din"
