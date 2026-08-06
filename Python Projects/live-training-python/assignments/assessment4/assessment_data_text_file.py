# 4.⁠ ⁠Write a program to create and write data into a text file, then read it back.
# 5.⁠ ⁠Write a program to store student information in a dictionary and display it.

def write_to_file(filename, text):
    try:
        with open(filename, "w") as f:
            f.write(text)
    except IOError as err:
        print(f"Failed to create file, {err}")

def read_file(filename):
    try:
        with open(filename) as f:
            text_info = f.read()
            print(f"Text File Output: {text_info}")
    except FileNotFoundError as err:
        print(f"Failure: File Not Found Error, {err}")
    

write_to_file("text_sample.txt", "This is a text file")
read_file("text_sample.txt")


students = {
    101: {"name": "Alice", "major": "Computer Science"},
    102: {"name": "Mark", "major": "English"},
    103: {"name": "Peter", "major": "Economics"}
}

for student_id, info in students.items():
    print(f"Student ID: {student_id} | Student Name: {info['name']} | Student Major: {info['major']}")