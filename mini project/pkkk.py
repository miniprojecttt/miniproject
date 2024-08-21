import nltk

# Download the 'punkt' tokenizer models
nltk.download('punkt')

import sqlite3

con = sqlite3.connect("database/apps.db")
cur = con.cursor()

cur.execute("CREATE TABLE app(appid, fraudulent, review);")