import pandas as pd
import sys

if len(sys.argv) > 3:
    dir_path = sys.argv[3]
else:
    dir_path = "."

if len(sys.argv) > 2:
    size = int(sys.argv[2])
else:
    size = 50000

if len(sys.argv) > 1:
    pure_file_name = sys.argv[1]
else:
    print("args: Herald_statements .")
    #pure_file_name= "mathlib_informal_v4.16.0"
    #pure_file_name= "Herald_proofs"
    #pure_file_name= "Herald_statements"

print(f"dir_path: {dir_path}")
print(f"pure_file_name: {pure_file_name}")
print(f"size: {size}")

jsonl_file_path = f"{dir_path}/{pure_file_name}.jsonl"

line_index = 0
file_index = 0
wf = open(f"{dir_path}/{pure_file_name}.{file_index}.jsonl", 'w', encoding='utf-8')
with open(jsonl_file_path, 'r', encoding='utf-8') as rf:
    for line in rf:
        if line_index > size:
            line_index = 0
            wf.close()
            file_index += 1
            wf = open(f"{dir_path}/{pure_file_name}.{file_index}.jsonl", 'w', encoding='utf-8')
        wf.write(line)
        wf.write("\n")
        line_index += 1
wf.close()

print(f"Successfully split '{jsonl_file_path}'")
