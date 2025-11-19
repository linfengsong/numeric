import psycopg
import os
import sys
import json
import dotenv

if len(sys.argv) > 1:
    table_name = sys.argv[1]
else:
    print("Need argument table name")
    exit(1)

if len(sys.argv) > 2:
    dir_path = sys.argv[2]
else:
    dir_path = "../data"

if len(sys.argv) > 3:
    dotenv_path = sys.argv[3]
else:
    dotenv_path = f"./.env"

sql = f"SELECT * FROM {table_name};"
output_path = f"{dir_path}/{table_name}.jsonl"

print(sql)
print(output_path)
print(dotenv_path)

dotenv.load_dotenv(dotenv_path=dotenv_path)

connect_str = os.environ["CONNECTION_STRING"]

print(connect_str)

conn = psycopg.connect(connect_str, autocommit=True)
cur = conn.cursor()

cur.execute(sql)
rows = cur.fetchall()

col_names = [desc[0] for desc in cur.description]

print(f"{col_names}")

with open(output_path, 'w', encoding='utf-8') as wf:
    for row in rows:
        rowObj = dict(zip(col_names, row))
        print(f"{rowObj}")
        json_output = json.dumps(rowObj)
        wf.write(json_output)
        wf.write("\n")

cur.close()
conn.close()
