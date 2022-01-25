import requests
from lxml import html
import time
from selenium import webdriver

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS csgo_predictor")
mycursor.execute("USE csgo_predictor")

#USE THIS TO CLEAR TABLE
#mycursor.execute("DROP TABLE matches_2021")
#mycursor.execute("DROP TABLE players_2021_dumb")
#mycursor.execute("DROP TABLE full_data_2021_dumb")

mycursor.execute("CREATE TABLE IF NOT EXISTS matches_2021 (id INTEGER AUTO_INCREMENT PRIMARY KEY, t1_p1_id INTEGER, t1_p1_name VARCHAR(255), t1_p2_id INTEGER, t1_p2_name VARCHAR(255), t1_p3_id INTEGER, t1_p3_name VARCHAR(255), t1_p4_id INTEGER, t1_p4_name VARCHAR(255), t1_p5_id INTEGER, t1_p5_name VARCHAR(255), t2_p1_id INTEGER, t2_p1_name VARCHAR(255), t2_p2_id INTEGER, t2_p2_name VARCHAR(255), t2_p3_id INTEGER, t2_p3_name VARCHAR(255), t2_p4_id INTEGER, t2_p4_name VARCHAR(255), t2_p5_id INTEGER, t2_p5_name VARCHAR(255), winner INTEGER)")

mycursor.execute("CREATE TABLE IF NOT EXISTS players_2021_dumb (id INTEGER PRIMARY KEY, name VARCHAR(255), rating_2 FLOAT)")

mycursor.execute("CREATE TABLE IF NOT EXISTS full_data_2021_dumb (id INTEGER PRIMARY KEY, t1_p1_rating_2 FLOAT, t1_p2_rating_2 FLOAT, t1_p3_rating_2 FLOAT, t1_p4_rating_2 FLOAT, t1_p5_rating_2 FLOAT, t2_p1_rating_2 FLOAT, t2_p2_rating_2 FLOAT, t2_p3_rating_2_0 FLOAT, t2_p4_rating_2 FLOAT, t2_p5_rating_2 FLOAT, winner INTEGER)")

# matches_2021 information
"""
matches_2021 information:

t1_p1_id INTEGER
t1_p1_name VARCHAR(255)
t1_p2_id INTEGER
t1_p2_name VARCHAR(255)
t1_p3_id INTEGER
t1_p3_name VARCHAR(255)
t1_p4_id INTEGER
t1_p4_name VARCHAR(255)
t1_p5_id INTEGER
t1_p5_name VARCHAR(255)

t2_p1_id INTEGER
t2_p1_name VARCHAR(255)
t2_p2_id INTEGER
t2_p2_name VARCHAR(255)
t2_p3_id INTEGER
t2_p3_name VARCHAR(255)
t2_p4_id INTEGER
t2_p4_name VARCHAR(255)
t2_p5_id INTEGER
t2_p5_name VARCHAR(255)

winner INTEGER
# 0 for team 1 winning, 1 for team 2 winning

"""
# players_2021_dumb
"""
players_2021 information:

Note that this data was obtained in early 2022

id INTEGER PRIMARY KEY
# should be identical to tX_pX_id in matches_2021
name VARCHAR(255)
# should be identical to tX_pX_name in matches_2021

rating_2.0 FLOAT
"""
# players_2021 information (not ipmlemented for now; just use rating 2.0 for first attempt)
"""
players_2021 information:

Note that this data was obtained in early 2022

id INTEGER PRIMARY KEY
# should be identical to tX_pX_id in matches_2021
name VARCHAR(2055)
# should be identical to tX_pX_name in matches_2021

# these entries are in "Overview"
kills INTEGER
headshots FLOAT
deaths INTEGER
k_d_ratio FLOAT
damage_per_round FLOAT
grenade_damage_per_round FLOAT
maps_plays INTEGER
rounds_player INTEGER
kills_per_round FLOAT
assists_per_round FLOAT
deaths_per_round FLOAT
saved_by_teammates FLOAT
saved_teammates FLOAT

rating_2.0 FLOAT

"""

# full_data_2021_dumb information
"""
full_data_2021 information:

id INTEGER PRIMARY KEY
# should be identical to primary key of matches_2021

t1_p1_rating_2 FLOAT
t1_p2_rating_2 FLOAT
t1_p3_rating_2 FLOAT
t1_p4_rating_2 FLOAT
t1_p5_rating_2 FLOAT

t2_p1_rating_2 FLOAT
t2_p2_rating_2 FLOAT
t2_p3_rating_2 FLOAT
t2_p4_rating_2 FLOAT
t2_p5_rating_2 FLOAT

winner INTEGER
# 0 for team 1 winning, 1 for team 2 winning
"""

# manually listed both pages for convenience
target_urls = ["https://www.hltv.org/results?startDate=2021-01-01&endDate=2021-12-31&stars=3", "https://www.hltv.org/results?offset=100&startDate=2021-01-01&endDate=2021-12-31&stars=3"]

# ordinary requests don't work because of javascript; selenium is required
"""
for i in range(len(target_urls)):
    page = requests.get(target_urls[i])
    page_HTML = html.fromstring(page.content)
    print(html.tostring(page_HTML))
    break
"""

browser = webdriver.Chrome()

for i in range(len(target_urls)):

    browser.get(target_urls[i])

    element = browser.find_element_by_xpath("//*")
    source_HTML = element.get_attribute("outerHTML")
    # print(source_HTML)