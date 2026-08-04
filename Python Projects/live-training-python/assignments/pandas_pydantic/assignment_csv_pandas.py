import csv
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [22, 43, 36],
    "city": ["New York", "Chicago", "LA"],
}

df = pd.DataFrame(data)
df.to_csv("assignments/output_panda.csv", index=False)
df.to_json("assignments/output_panda.json", index=False, indent=2)




