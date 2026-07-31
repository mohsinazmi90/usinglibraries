import csv
import json
import os
from typing import List, Dict, Any


class DataProcessingPipeline:
    def __init__(self, input_csv: str, output_json: str):
        self.input_csv = input_csv
        self.output_json = output_json

    def extract(self) -> List[Dict[str, str]]:
        if not os.path.exists(self.input_csv):
            raise FileNotFoundError(f"File not found: {self.input_csv}")

        records = []
        with open(self.input_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row_idx, row in enumerate(reader, start=1):
                # Handles headers with whitespace or differing cases
                row_clean = {k.strip().lower(): v for k, v in row.items() if k}
                if not row_clean.get("id"):
                    print(
                        f"[WARN]: Row {row_idx} skipped due to missing primary key 'id'"
                    )
                    continue
                records.append(row_clean)
        return records

    def transform(self, records: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        transformed = []
        for row in records:
            try:
                transformed.append(
                    {
                        "id": int(row["id"]),
                        "name": row["name"].strip().title(),
                        "salary": float(row["salary"]),
                    }
                )
            except (KeyError, ValueError) as err:
                print(f"[SKIP]: Data conversion failure in record {row}: {err}")

        return transformed

    def load(self, data: List[Dict[str, Any]]) -> None:
        try:
            with open(self.output_json, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except IOError as error:
            print(f"[CRITICAL]: Write operation failed: {error}")
            raise

    def run(self) -> bool:
        print("Starting data pipeline execution...")
        try:
            raw_data = self.extract()
            processed_data = self.transform(raw_data)
            self.load(processed_data)
        except Exception as err:
            print(f"[FAILURE]: Pipeline execution halted unexpectedly: {err}")
            return False
        else:
            print(
                f"[SUCCESS]: Processed {len(processed_data)} item(s). Saved to '{self.output_json}'."
            )
            return True
        finally:
            print("Pipeline run finalized.")


# --- EXECUTION SETUP AND TESTING

# 1. SETUP MOCK CSV FILE WITH VALID AND INVALID ROWS
mock_csv_content = "ID, Name, Salary1, John Doe, 75000.50"
"2, James Smith, Invalid_Salary, Broken User, 50000.00"
"3, Alice Walk, 92000.00"

with open("employees_raw.csv", "w", encoding="UTF-8") as f:
    f.write(mock_csv_content)

# 2. EXECUTE PIPELINE
pipeline = DataProcessingPipeline("employees_raw.csv", "employees_clean.json")

pipeline.run()

# import csv
# import json
# import os
# from typing import List, Dict, Any


# class DataProcessingPipeline:
#     def __init__(self, input_csv: str, output_json: str):
#         self.input_csv = input_csv
#         self.output_json = output_json

#     def extract(self) -> list[dict[str, str]]:
#         if not os.path.exists(self.input_csv):
#             raise FileNotFoundError(self.input_csv)

#         records = []
#         with open(self.input_csv, "r", encoding="UTF-8") as f:
#             reader = csv.DictReader(f)
#             for row_idx, row in enumerate(reader, start=1):
#                 if not row.get("id"):
#                     print(f"[WARN]: {row_idx} skipped due to missing primary key, ID")
#                     continue
#                 records.append(dict[row])
#         return records

#     def transform(self, record: list[dict[str, str]]) -> list[dict[str, Any]]:
#         transform = []
#         for row in record:
#             try:
#                 transform.append(
#                     {
#                         "ID": int(row["id"]),
#                         "Name": row["name".strip().title()],
#                         "Salary": float(row["salary"]),
#                     }
#                 )
#             except KeyError:
#                 print(f"[SKIP]: Data conversion failure in record {row}: {KeyError}")
#                 return transform

#     def load(self, data: list[dict[str, Any]]) -> None:
#         try:
#             with open(self.output_json, "w", encoding="UTF-8)") as f:
#                 json.dump(data, f, indent=4)
#         except IOError as error:
#             print(f"[CRITICAL]: This write failed {error}")
#             raise

#     def run(self) -> bool:
#         print("Starting data pipeline execution")
#         try:
#             raw_data = self.extract()
#             processed_data = self.transform(raw_data)
#             self.load(processed_data)
#         except Exception as err:
#             print(f"[FAILURE]: Pipeline execution halted unexpectedly, {err}")
#             return False
#         else:
#             print(
#                 f"[SUCCESS]: Processed {len(processed_data)}. Item saved to {self.output_json}."
#             )
#             return True
#         finally:
#             print("Pipeline run finalized.")


# --- EXECUTION SETUP AND TESTING

# # 1. SETUP MOCK CSV FILE WITH VALID AND INVALID ROWS
# mock_csv_content = "ID, Name, Salary1, John Doe, 75000.50"
# "2, James Smith, Invalid_Salary, Broken User, 50000.00"
# "3, Alice Walk, 92000.00"

# with open("employees_raw.csv", "w", encoding="UTF-8") as f:
#     f.write(mock_csv_content)

# # 2. EXECUTE PIPELINE
# pipeline = DataProcessingPipeline("employees_raw.csv", "employees_clean.json")

# pipeline.run()


# import csv
# import json
# import os
# from typing import List, Dict, Any


# class DataProcessingPipeline:
#     def _init_(self, input_csv: str, output_json: str):
#         self.input_csv = input_csv
#         self.output_json = output_json

#     def extract(self) -> List[Dict[str, str]]:
#         if not os.path.exists(self.input_csv):
#             raise FileNotFoundError(f"File not found: {self.input_csv}")

#         records = []
#         with open(self.input_csv, "r", encoding="utf-8") as f:
#             reader = csv.DictReader(f)
#             for row_idx, row in enumerate(reader, start=1):
#                 # Handles headers with whitespace or differing cases
#                 row_clean = {k.strip().lower(): v for k, v in row.items() if k}
#                 if not row_clean.get("id"):
#                     print(
#                         f"[WARN]: Row {row_idx} skipped due to missing primary key 'id'"
#                     )
#                     continue
#                 records.append(row_clean)
#         return records

#     def transform(self, records: List[Dict[str, str]]) -> List[Dict[str, Any]]:
#         transformed = []
#         for row in records:
#             try:
#                 transformed.append(
#                     {
#                         "id": int(row["id"]),
#                         "name": row["name"].strip().title(),
#                         "salary": float(row["salary"]),
#                     }
#                 )
#             except (KeyError, ValueError) as err:
#                 print(f"[SKIP]: Data conversion failure in record {row}: {err}")

#         return transformed

#     def load(self, data: List[Dict[str, Any]]) -> None:
#         try:
#             with open(self.output_json, "w", encoding="utf-8") as f:
#                 json.dump(data, f, indent=4)
#         except IOError as error:
#             print(f"[CRITICAL]: Write operation failed: {error}")
#             raise

#     def run(self) -> bool:
#         print("Starting data pipeline execution...")
#         try:
#             raw_data = self.extract()
#             processed_data = self.transform(raw_data)
#             self.load(processed_data)
#         except Exception as err:
#             print(f"[FAILURE]: Pipeline execution halted unexpectedly: {err}")
#             return False
#         else:
#             print(
#                 f"[SUCCESS]: Processed {len(processed_data)} item(s). Saved to '{self.output_json}'."
#             )
#             return True
#         finally:
#             print("Pipeline run finalized.")
