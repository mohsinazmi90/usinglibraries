import json
import os

# --- 1. PREPARE DATA STRUCTURE ---
dataset = {
    "company": "TechCorp",
    "established": 2018,
    "employees": [
        {
            "id": 101,
            "name": "John Doe",
            "department": "Engineering",
            "skills": ["Python", "SQL", "Docker"],
            "salary": 75000.50,
            "is_remote": True,
        },
        {
            "id": 102,
            "name": "Alice Walk",
            "department": "Data Science",
            "skills": ["Python", "Pandas", "PyTorch"],
            "salary": 92000.00,
            "is_remote": False,
        },
    ],
}

file_path = "company_data.json"


# --- 2. WRITE TO JSON FILE (DEVELOPMENT / SAVING) ---
def save_json_file(path: str, data: dict) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            # indent=4 formats the output cleanly with spacing
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"[SUCCESS]: Data saved to '{path}'.")
    except IOError as err:
        print(f"[ERROR]: Failed to write file: {err}")


# --- 3. READ & PARSE JSON FILE ---
def read_json_file(path: str) -> dict:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Target file missing: '{path}'")

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = json.load(f)
            return content
    except json.JSONDecodeError as err:
        print(f"[ERROR]: Invalid JSON format in '{path}': {err}")
        return {}


# --- 4. UPDATE & MODIFY JSON CONTENT ---
def append_employee(path: str, new_employee: dict) -> None:
    data = read_json_file(path)
    if data:
        data["employees"].append(new_employee)
        save_json_file(path, data)


# --- EXECUTION ---
if __name__ == "_main_":
    # Create file
    save_json_file(file_path, dataset)

    # Read back and output a specific value
    current_data = read_json_file(file_path)
    print("\nFirst Employee Name:", current_data["employees"][0]["name"])

    # Append a new record and update file
    new_hire = {
        "id": 103,
        "name": "Robert Chen",
        "department": "DevOps",
        "skills": ["AWS", "Kubernetes"],
        "salary": 88000.00,
        "is_remote": True,
    }
