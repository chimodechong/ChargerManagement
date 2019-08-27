"""
提供一个从json文件读取信息的函数
"""
import json

def get_json_records(filename):
    json_file = open(filename, "r")
    content = json.loads(json_file.read())
    json_file.close()
    return content

# assume {str:int}
def print_dict(record_dict):
    for key in record_dict.keys():
        print(key, end=": ")
        print(record_dict[key], end=" ")

# assume record is a tuple/list containing two dicts
def print_records(records):
    for record in records:
        print_dict(record[0])
        print("----> ", end="")
        print_dict(record[1])
        print()