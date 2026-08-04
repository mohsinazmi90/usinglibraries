import json
# from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError
from pathlib import Path

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
    skills: list[str] = Field(default_factory=list)
    
    
def save_employee_to_json(employee, file_name: str | Path):
    json_data = employee.model_dump_json(indent=4)
    with open(file_name, "w", encoding="UTF-8") as f:
        f.write(json_data)
    
    print(f"Emoloyee saved successfully to {file_name}")
    
def load_file_from_json(file_name: str):
    try:
        with open(file_name, "r", encoding="UTF-8") as f:
            file_content = f.read()
            employee = Employee.model_validate_json(file_content)
            return employee
    except FileNotFoundError:
        print(f"File: {file_name} not found.")
    except ValidationError as e:
        print(f"Validation Error: {e}.")
    except json.JSONDecodeError:
        print(f"Error: File contains invalid JSON syntax.")
        return None
        
if __name__ == "__main__":
    emp = Employee(
        id = 101,
        name = "Sara Connor",
        email = "sara.connor@example.com",
        role = "Lead Engineer",
        address = Address(street="123 Tech House", city="New York", zip_code="11355"),
        skills = ["Python", "Pydantic", "FastAPI"]
    )

    file_name = "assignments/Pandas_Pydantic/student_employee_data.json"
    path = Path(file_name)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    save_employee_to_json(emp, path)
    
    loaded_employee_from_json = load_file_from_json(file_name)
    if loaded_employee_from_json:
        print(f"Loaded Profile: Name: {loaded_employee_from_json.name}, Email: {loaded_employee_from_json.email}, City: {loaded_employee_from_json.address.city}")
        