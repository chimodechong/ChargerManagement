import data_handling
import os
import json

file_names = []

def search_file_names():
    # add root path for data here
    file_path = "d:\\temp_data\\"
    for i,j,k in os.walk(file_path):
        if len(k) > 0:
            for file_name in k:
                if file_name[-4:] == ".txt":
                    file_names.append(i + "\\" + file_name)

def form_record(record):
    record_now = record[0]
    record_then = record[1]
    new_record_now = dict()
    new_record_then = dict()

    new_record_now["icv"] = int(record_now[0])
    new_record_now["ici"] = int(record_now[1])
    new_record_now["ibv"] = int(record_now[2])
    new_record_now["ibt"] = int(record_now[3])
    new_record_now["itt"] = int(record_now[4])
    new_record_now["freq"] = int(record_now[5])
    new_record_now["temp_th"] = int(record_now[6])
    new_record_then["ibt"] = int(record_then[0])
    new_record_then["itt"] = int(record_then[1])

    return (new_record_now, new_record_then)


def main():
    json_file = open("d:/Temp_data/results.json", "w")
    records = []
    record_num = 0

    """更改数据过滤和处理方法仅需修改下两行"""
    iterator_factory = data_handling.IPGDataIteratorFactory()  # determine rough filter
    factory = data_handling.SecondFilterFactory() # determine how data processed


    for file_name in file_names:
        print("handling: " + file_name)

        data_iterator = iterator_factory.create_iterator()
        product = factory.create_product(data_iterator)

        product.read_data(file_name)
        product.process_data()
        for data_record in product.show_result():
            record_num += 1
            #print("record: " + str(record_num))
            try:
                records.append(form_record(data_record))
            except:
                print("mem err exit: record: " + str(record_num))
                os._exit(-1)
        print("total records: " + str(record_num))
    json_file.write(json.dumps(records))
    json_file.close()

if __name__ == "__main__":
    search_file_names()
    #print(file_names)
    main()
