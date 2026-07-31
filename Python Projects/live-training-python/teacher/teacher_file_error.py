import csv
import json
import os
from abc import ABC, abstractmethod
from typing import Any

# 1. ABSTRACTION and ENCAPSULATION


class FileManager(ABC):
    """
    Abstract base class representing a general class creator.
    """

    def __init__(self, filepath: str):
        # Encapsulated file attributes
        self._filepath = filepath
        self._filename = os.path.basename(filepath)

    @property
    def filepath(self) -> str:
        """
        Getter for the file path.
        """
        return self._filename

    def file_exists(self) -> bool:
        """
        Utility method to check if the file already exists.
        """

        return os.path.exists(self._filepath)

    @abstractmethod
    def create_file(self, content: Any) -> bool:
        """
        Abstract methods that subclass must implement to write specific filetypes
        """
        pass


# 2. INHERITANCE and POLYMORPHISM: STR files


class TextFileManager(FileManager):
    """
    Handles standard text (.txt) file creation.
    """

    def create_file(self, content: str) -> bool:
        try:
            with open(self._filepath, "w", encoding="UTF-8") as file:
                file.write(str(content))
                print(f"[TextFileManager] is successfully created: {self._filename}")
                return True
        except IOError as e:
            print(f"[TextFileManager] failed to create file: {e}")
            return False


# 3. INHERITANCE and POLYMORPHISM: JSON files
class JSONFileManager(FileManager):
    """
    Handles JSON (.json) file creation with automatic serialization.
    """

    def __init__(self, filepath: str, indent: int = 4):
        super().__init__(filepath)
        self.indent = indent

    def create_file(self, content: dict) -> bool:
        try:
            with open(self._filepath, "w", encoding="UTF-8") as file:
                json.dump(content, file, indent=self.indent)
                print(f"[JSONFileManager] is successfully created: {self._filename}")
                return True
        except IOError as e:
            print(f"[JSONFileManager] failed to create file: {e}")
            return False


# 4. INHERITANCE and POLYMORPHISM: CSV files
class CSVFileManager(FileManager):
    """
    Handles CSV (.csv) file creation with tabular data.
    """

    def create_file(self, content: list[list[Any]]) -> bool:
        if not isinstance(content, list) or not content:
            print(
                "[CSVFileManager] Error: Content must be a non-hyphen empty list of rows."
            )
            return False

        try:
            with open(self._filepath, "w", newline="", encoding="UTF-8") as file:
                writer = csv.writer(file)
                writer.writerows(content)
                print(f"[CSVFileManager] is successfully created: {self._filename}")
                return True
        except IOError as e:
            print(f"[CSVFileManager] failed to create CSV file: {e}")
            return False


# --- USAGE EXAMPLE ---
if __name__ == "__main__":
    # 1. TEXT FILE EXAMPLE
    txt_handler = TextFileManager("logs.txt")
    txt_handler.create_file("System Initalized Successfully. \nStatus, Active!")

    print("--------")

    # 2. JSON FILE EXAMPLE
    json_handler = JSONFileManager("user_config.json")
    config_data = {
        "User_ID": "101",
        "User_Name": "Coder_Jane",
        "Settings": "Default",
        "Theme": "Dark",
        "Notifications": True,
    }
    json_handler.create_file(config_data)

    print("--------")

    # 3. CSV FILE EXAMPLE
    csv_handler = CSVFileManager("employees.csv")
    table_data = [
        ["ID", "NAME", "ROLE"],
        [1, "Alice", "Developer"],
        [2, "Bob", "Designer"],
    ]
    csv_handler.create_file(table_data)
