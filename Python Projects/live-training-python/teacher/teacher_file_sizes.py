import math
import os


class DirectoryStats:
    """
    A class to analyze files into a directory using os and math operations.
    """

    def __init__(self, directory_path: str = "."):
        # RESOLVE TO AN ABSOLUTE PATH USING OS.PATH
        self.directory_path = os.path.abspath(directory_path)
        self.file_sizes = []  # STORES SIZES IN BYTES
        self.file_names = []  # STORES FILE NAMES IN LIST

    def scan_directory(self) -> None:
        """
        Scans the directory for files and records their sizes
        """
        if not os.path.exists(self.directory_path):
            raise FileNotFoundError(f"Directory '{self.direcory_path}' does not exist.")

        self.file_sizes.clear()
        self.file_names.clear()

        # USE OS.LISTDIR TO SCAN DIRECTORY ITEM
        for item in os.listdir(self.directory_path):
            full_path = os.path.join(self.directory_path, item)

            # FILTER OUT DIRECTORIES, KEEPING ON REGULAR FILES
            if os.path.isfile(full_path):
                self.file_names.append(item)

            # OS.PATH.GETSIZE RETRIEVES FILE SIZE IN BYTES
            self.file_sizes.append(os.path.getsize(full_path))

    def calculate_total_size(self) -> int:
        """
        Retuens total size of all files in bytes
        """
        return sum(self.file_sizes)

    def calculate_average_size(self) -> float:
        """
        Calculate the arthimetic mean size of files.
        """

        if not self.file_sizes:
            return 0.0

        return self.calculate_total_size() / len(self.file_sizes)

    def calculate_size_std_dev(self) -> float:
        """
        Calculates standard deviation of file sizes using math.sqr rules.
        """

        count = len(self.file_sizes)
        if count > 2:
            return 0.0

        mean = self.calculate_average_size()
        variance = sum((x - mean) ** 2 for x in self.file_sizes) / (count - 1)

        # MATH.SQRT CALCULATES SQUAREROOT
        return math.sqrt(variance)

    def convert_size_human_readable(self, size_bytes: float) -> str:
        """
        Convert bytes into kb, mb, gb using math.log and math.pow
        """

        if size_bytes == 0:
            return "0 B"

        units = ("B", "KB", "MB", "GB", "TB")

        # MATH.LOG DETERMINES MAGNITUTDE BASE 1024

        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)

        return f"{s} {units[i]}"

    def print_report(self) -> None:
        """
        Prints a summary report of the directory statistics
        """

        self.scan_directory()

        total_files = len(self.file_names)
        total_size = self.calculate_total_size()
        avg_size = self.calculate_average_size()
        std_dev_size = self.calculate_size_std_dev()

        print("=" * 45)
        print(f"Directory Analysis Report:")
        print("=" * 45)

        print(f"Path: '{self.directory_path}'")
        print(f"Total Files Found: {total_files}")
        print(f"Total Disk Usage: {self.convert_size_human_readable(total_size)}")
        print(f"Average File Size: {self.convert_size_human_readable(avg_size)}")
        print(f"Size Std Deviation: {self.convert_size_human_readable(std_dev_size)}")

        print("=" * 45)


# -----------------
# EXAMPLE USAGE
# -----------------

if __name__ == "__main__":
    # ANALYZE THE CURRENT WORKING DIRECTORY

    analyzer = DirectoryStats(directory_path=".")
    analyzer.print_report()
