import csv
import pandas as pd

# WRITE TO CSV FILE USING CSV
# DATA TO WRITE
# data = [
#     ["Name", "Age", "City"],
#     ["Alice", 28, "New York"],
#     ["Bob", 34, "San Francisco"],
#     ["Charlie", 22, "France"],
# ]

# # WRITE TO CSV
# with open("output.csv", mode="w", newline="", encoding="UTF-8") as f:
#     writer = csv.writer(f)
#     writer.writerows(data)
#     print("CSV file created successfully")

# WRITE TO CSV FILE USING PANDAS
data = {
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
    ],
    "Age": [
        28,
        34,
        22,
    ],
    "City": [
        "New York",
        "San Francisco",
        "France",
    ],
}

df = pd.DataFrame(data)
df.to_csv("output_pandas.csv", index=False)
df.to_json("output.json", indent=False)
