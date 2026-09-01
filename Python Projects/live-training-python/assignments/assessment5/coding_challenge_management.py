import csv
import json
import sqlite3
from typing import List, Optional, Dict, Any

class Student:
    def __init__(self, student_id: int, name: str, age: int, grade: str):
        if not isinstance(student_id, int) or student_id <= 0:
            raise ValueError("student_id must be a positive integer.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("age must be a positive integer.")
        if not name.strip() or not grade.strip():
            raise ValueError("name and grade cannot be empty.")
            
        self.student_id = student_id
        self.name = name.strip()
        self.age = age
        self.grade = grade.strip()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

    def __repr__(self) -> str:
        return f"Student(id={self.student_id}, name='{self.name}', age={self.age}, grade='{self.grade}')"


class StudentManagementSystem:
    def __init__(self, db_name: str = "students.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self._create_table()

    def _create_table(self):
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS students (
                        student_id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        grade TEXT NOT NULL
                    )
                ''')
        except sqlite3.Error as e:
            raise StudentError(f"Database initialization failed: {e}")

    def add_student(self, student: Student):
        try:
            with self.conn:
                self.conn.execute(
                    'INSERT INTO students (student_id, name, age, grade) VALUES (?, ?, ?, ?)',
                    (student.student_id, student.name, student.age, student.grade)
                )
        except sqlite3.IntegrityError:
            raise StudentError(f"Student with ID {student.student_id} already exists.")
        except sqlite3.Error as e:
            raise StudentError(f"Failed to add student: {e}")

    def get_student(self, student_id: int) -> Optional[Student]:
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT student_id, name, age, grade FROM students WHERE student_id = ?', (student_id,))
            row = cursor.fetchone()
            return Student(*row) if row else None
        except sqlite3.Error as e:
            raise StudentError(f"Failed to retrieve student: {e}")

    def update_student(self, student: Student):
        try:
            with self.conn:
                cursor = self.conn.execute(
                    'UPDATE students SET name = ?, age = ?, grade = ? WHERE student_id = ?',
                    (student.name, student.age, student.grade, student.student_id)
                )
                if cursor.rowcount == 0:
                    raise StudentError(f"Cannot update: No student found with ID {student.student_id}.")
        except sqlite3.Error as e:
            raise StudentError(f"Database error during update: {e}")

    def delete_student(self, student_id: int):
        try:
            with self.conn:
                cursor = self.conn.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
                if cursor.rowcount == 0:
                    raise StudentError(f"Cannot delete: No student found with ID {student_id}.")
        except sqlite3.Error as e:
            raise StudentError(f"Database error during deletion: {e}")

    def list_students(self) -> List[Student]:
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT student_id, name, age, grade FROM students')
            return [Student(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise StudentError(f"Failed to list students: {e}")

    def export_to_csv(self, file_name: str):
        try:
            students = self.list_students()
            with open(file_name, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=["student_id", "name", "age", "grade"])
                writer.writeheader()
                for s in students:
                    writer.writerow(s.to_dict())
        except (IOError, StudentError) as e:
            raise StudentError(f"CSV Export failed: {e}")

    def export_to_json(self, file_name: str):
        try:
            students = self.list_students()
            with open(file_name, mode='w', encoding='utf-8') as f:
                json.dump([s.to_dict() for s in students], f, indent=4)
        except (IOError, StudentError) as e:
            raise StudentError(f"JSON Export failed: {e}")

    def import_from_csv(self, file_name: str):
        try:
            with open(file_name, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    student = Student(int(row["student_id"]), row["name"], int(row["age"]), row["grade"])
                    try:
                        self.add_student(student)
                    except StudentError:
                        pass  # Skip duplicates on import
        except Exception as e:
            raise StudentError(f"CSV Import failed: {e}")

    def import_from_json(self, file_name: str):
        try:
            with open(file_name, mode='r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    student = Student(int(item["student_id"]), item["name"], int(item["age"]), item["grade"])
                    try:
                        self.add_student(student)
                    except StudentError:
                        pass  # Skip duplicates on import
        except Exception as e:
            raise StudentError(f"JSON Import failed: {e}")

    def close(self):
        if self.conn:
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


if __name__ == "__main__":
    # Context manager automatically handles closing the connection
    with StudentManagementSystem(":memory:") as sms:
        sms.add_student(Student(1, "Alice", 20, "A"))
        sms.add_student(Student(2, "Bob", 21, "B"))
        sms.add_student(Student(3, "Charlie", 22, "C"))
        sms.update_student(Student(2, "Bob", 22, "A"))
        sms.delete_student(3)
        sms.add_student(Student(4, "Diana", 23, "B"))
        sms.add_student(Student(5, "Ethan", 24, "C"))
        sms.add_student(Student(6, "Fiona", 25, "A"))
        sms.add_student(Student(7, "George", 26, "B"))

        print("Current Students:")
        print(sms.list_students())

        sms.export_to_csv("students.csv")
        sms.export_to_json("students.json")