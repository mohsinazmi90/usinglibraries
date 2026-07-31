import json
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError

# -------------------
# 1. DEFINE YOUR DATA MODELS (DATA FRAMEWORK)
# -------------------


class Address(BaseModel):
    street: str
    city: str
    zip_code: str = Field(pattern=r"^\d{5}$", description="5-digits us zipcode")


class Employee(BaseModel):
    id: int
    name: str
    email: str
    role: str = "Developer"
    address: Address
    skills: List[str] = [[]]


# -------------------
# 2. WRITE DEVELOP DATA TO A JSON FILE
# -------------------
def save_employee_to_json(employee, file_name: str):
    """
    SERIALIZES A PYDANTIC MODEL DIRECTLY TO A FORMATTED JSON FILE.
    """

    # MODEL_DUMP_JSON (HANDLES FORMATTING AND SERIALIZING SEEMLESSLY)
    json_data = employee.model_dump_json(indent=2)
    with open(file_name, "w", encoding="UTF-8") as f:
        f.write(json_data)

    print(f"Successfully saved data to {file_name}")


# -------------------
# 3. READ AND VALIDATE JSON FILE DATA
# -------------------
def load_employee_from_json(file_name: str) -> Optional:
    """
    READ A JSON FILE AND PARSES IT AND VALIDATES INTO A PYDANTIC FORMAT
    """
    try:
        with open(file_name, "r", encoding="UTF-8") as f:
            file_content = f.read()
            # MODEL_VALIDATE_JSON DIRECTLY PRASES RAW JSON STRING
            employee = Employee.model_validate_json(file_content)
            return employee
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    except ValidationError as e:
        print(f"❌ Validation Error while loading JSON data:\n{e}")
    except json.JSONDecodeError:
        print("❌ Error: File contains invalid JSON syntax.")
        return None


# -------------------
# CODE.RUN EXAMPLE
# -------------------

if __name__ == "__main__":
    # CREATES AN EMPLOYEE INSTANCE (PYDANTIC VALIDATES FIELD ON INSTANTATION)

    emp = Employee(
        id=1001,
        name="Sara Connor",
        email="sara.connor@example.com",
        role="Lead Engineer",
        address=Address(
            street="123 Tech House", city="New York", zip_code="71701"
        ),  # VALIDATES AGAINST 5_DIGITS REGEX,
        skills=["Python", "Pydantic", "FastAPI"],
    )

    file_name = "employee_data.json"
    save_employee_to_json(emp, file_name)

    # LOAD BACK FROM FILE
    loaded_emp_from_json = load_employee_from_json(file_name)
    if loaded_emp_from_json:
        print(
            f"\nLoaded profile: {loaded_emp_from_json.name}, {loaded_emp_from_json.email}, {loaded_emp_from_json.address.city}"
        )
