import json
import sys

def parse_record(record):
    record = json.loads(stripped_line)
    id = record["id"]
    formal_statement = record["formal_statement"]
    informal_statement = record["informal_statement"]
    name = None
    if formal_statement:
        lines = formal_statement.replace("\t", " ").splitlines()
        for line in lines:
            line = line.strip()
            if line:
                if line.startswith("import ") or line.startswith("from ") or line.startswith("open "):
                    continue
                if line.startswith("noncomputable "):
                    line = line[14:]
                if line.startswith("private "):
                    line = line[8:]
                if line.startswith("protected "):
                    line = line[10:]
                if line.startswith("public "):
                    line = line[7:]
                name = line
        if name == None:
            print(f"Error parse line: {formal_statement}")
    else:
        print(f"Error formal_statement does not exist: {stripped_line}")
    return id, name, informal_statement

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

jsonl_file_path = f"{dir_path}/{pure_file_name}.jsonl"
csv_file_path = f"{dir_path}/{pure_file_name}.name.csv"

print(f"dir_path: {dir_path}")
print(f"pure_file_name: {pure_file_name}")

output_list = []
with open(jsonl_file_path, 'r', encoding='utf-8') as rf:
    for line in rf:
        stripped_line = line.strip()
        if stripped_line:
            try:
                record = json.loads(stripped_line)
                id, name, informal_statement = parse_record(record)
                if name == None:
                    print(f"Error parse line: {stripped_line}")
                wline = f"{name},{id}, {informal_statement}"               
                output_list.append(wline)
            except json.JSONDecodeError:
                print(f"Error decoding JSON on line: {stripped_line}")
output_list.sort()
with open(csv_file_path, 'w', encoding='utf-8') as wf:
    for line in output_list:
        print(line)
        wf.write(line)
        wf.write("\n")
print(f"Successfully converted '{jsonl_file_path}' to '{csv_file_path}'")