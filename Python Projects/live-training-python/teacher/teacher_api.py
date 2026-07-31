import requests  # THIS IS USED TO INTERACT WITH APIs
import json

# FETCH PUBLIC DATA FROM AN API ENDPOINT
response = requests.get("https://api.github.com/users/octocat")

# CHECK IF THE REQUEST SUCCEEDED (STATUS CODE 200)
if response.status_code == 200:
    data = response.json()
    print(data["name"])


# Standard JSON formatted string (booleans are lowercase: true/false)
raw_json = '{"Name": "Alice", "Role": "Developer", "Active": "true"}'

# CONVERTS JSON STRINGS TO PYTHON DICTIONARY
user_dict = json.loads(raw_json)
print(user_dict["Name"])

# CONVERT PYTHON DICTIONARY BACK TO JSON STRING
# json_string = json.dumps(user_dict, indent=2)
with open("JSON_Test.json", "w", encoding="UTF-8") as f:
    json.dump(user_dict, f, indent=4)


# import json

# # Standard JSON formatted string (booleans are lowercase: true/false)
# raw_json = '{"Name": "Alice", "Role": "Developer", "Active": true}'

# # Convert JSON string to Python dictionary
# user_dict = json.loads(raw_json)

# # Access dictionary value
# print(f"Name from dict: {user_dict['Name']}")

# # Convert Python dictionary back to a JSON string (in memory)
# json_string = json.dumps(user_dict, indent=4)
# print("\nJSON String output:")
# print(json_string)

# # Save Python dictionary directly to a .json file
# with open("JSON_Test.json", "w", encoding="utf-8") as f:
#     json.dump(user_dict, f, indent=4)
