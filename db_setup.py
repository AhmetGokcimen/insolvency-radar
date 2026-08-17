import sqlite3
import json

conn = sqlite3.connect("insolvency.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ads (
    id INTEGER PRIMARY KEY,
    category TEXT,
    title TEXT,
    advertiser_name TEXT,
    city TEXT,
    county TEXT,
    publish_date TEXT,
    url TEXT,
    decision_type_id INTEGER NULL,
    decision_type_name TEXT NULL,
    predicted_label TEXT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ad_vkn (
    id INTEGER PRIMARY KEY,
    ad_id INTEGER,
    vkn TEXT,
    FOREIGN KEY (ad_id) REFERENCES ads (id)
)
""")

conn.commit()
conn.close()