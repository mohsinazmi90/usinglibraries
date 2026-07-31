import os
from datetime import datetime, timedelta
import random
import math

# ----------------------------
#          OS MODULE
# ----------------------------

# GET CURRENT WORKING DIRECTORY
print(os.getcwd())

# CREATE A NEW FOLDER SAFELY USING 'OS' MODULE
os.makedirs("my_folder", exist_ok=True)

# ----------------------------
#       DATETIME MODULE
# ----------------------------

# GET OS TIME FROM DATETIME
now = datetime.now()
print(f"Current Time: {now.strftime('("%Y-%m-%d %H:%M")')}\n")

# ADD 7 DAYS FROM THE CURRENT DATE
next_week = now + timedelta(days=7)
print(f"Next Week Time: {next_week.strftime('("%Y-%m-%d %H:%M")')}\n")

# ----------------------------
#       RANDOM MODULE
# ----------------------------

# GENERATE A RANDOM INTEGER BETWEEN 1 AND 10
# PICK A RANDOM ITEM FROM A LIST
choices = ["Apple", "Banana", "Cherry", "Durian"]
picked = random.choice(choices)
print(f"Random Choice Picked: {picked}\n")


# ----------------------------
#       MATH MODULE
# ----------------------------
print(math.sqrt(64))
print(math.ceil(4.2))
print(math.pi)
