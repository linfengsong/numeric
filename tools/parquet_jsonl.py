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
    #pure_file_name= "Herald_proofs"
    #pure_file_name= "Herald_statements"

print(f"dir_path: {dir_path}")
print(f"pure_file_name: {pure_file_name}")

parquet_file_path = f"{dir_path}/{pure_file_name}.parquet"
jsonl_output_path= f"{dir_path}/{pure_file_name}.jsonl"
df = pd.read_parquet(parquet_file_path, engine='pyarrow')
df.to_json(jsonl_output_path, orient='records', lines=True)

print(f"Successfully converted '{parquet_file_path}' to '{jsonl_output_path}'")
