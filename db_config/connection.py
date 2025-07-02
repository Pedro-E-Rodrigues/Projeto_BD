import os
from arango import ArangoClient
from dotenv import load_dotenv

load_dotenv()
client = ArangoClient(hosts=os.getenv("ARANGO_HOST"))
db = client.db(
    os.getenv("DB_NAME"),
    username=os.getenv("ARANGO_USER"),
    password=os.getenv("ARANGO_PASS")
)
