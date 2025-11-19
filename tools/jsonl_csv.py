import pandas as pd
import sys

if len(sys.argv) > 2:
    dir_path = sys.argv[2]
else:
    dir_path = "."

if len(sys.argv) > 1:
    pure_file_name = sys.argv[1]
else:
    print("args: Herald_statements .")
    #pure_file_name= "mathlib_informal_v4.16.0"
    #pure_file_name= "Herald_proofs"
    #pure_file_name= "Herald_statements"

print(f"dir_path: {dir_path}")
print(f"pure_file_name: {pure_file_name}")

jsonl_file_path = f"{dir_path}/{pure_file_name}.jsonl"
csv_file_path = f"{dir_path}/{pure_file_name}.csv"

df = pd.read_json(jsonl_file_path, lines=True)

df.to_csv(csv_file_path, index=False)

print(f"Successfully converted '{jsonl_file_path}' to '{csv_file_path}'")