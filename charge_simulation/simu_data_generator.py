import simulation_filters
import recordslib
import datavisuallib
import json
 
def generate_json_records(records):
    """
    input: list[ tuple( dict{ now_data }, dict{ then_data } ) ]
    output: dict{ { (ibt*1000 + itt): dict{ (ibt_then*1000 + itt_then): num_of_appearance } }
    这样存是因为json仅允许key为整数，浮点，字符串等，不允许元组
    """
    result = dict()
    for record in records:
        key = record[0]["ibt"]*1000 + record[0]["itt"]
        if key in result.keys():
            key2 = record[1]["ibt"]*1000 + record[1]["itt"]
            if key2 in result[key].keys():
                result[key][key2] += 1
            else:
                result[key][key2] = 1
        else:
            result[key] = {record[1]["ibt"]*1000 + record[1]["itt"] : 1}
    return result


def save_records(filename, records):
    json_file = open(filename, "w")
    json_file.write(json.dumps(records))
    json_file.close()


def main():
    print("starting program")
    records_part1 = recordslib.get_json_records("D:/Temp_data/results1.json")
    records_part2 = recordslib.get_json_records("D:/Temp_data/results2.json")
    records_part3 = recordslib.get_json_records("D:/Temp_data/results3.json")
    records_part4 = recordslib.get_json_records("D:/Temp_data/results4.json")
    records = records_part1 + records_part2 + records_part3 + records_part4
    print("records got")

    """
    10mA 部分
    """
    # init filters
    filter_one = simulation_filters.ZeroMaFilter()
    filter_two = simulation_filters.C34RecordsFilter()
    filter_three = simulation_filters.ZeroMaGenFilter()
    
    # set input records
    filter_one.set_records(records)
    # chain filters
    filter_one.set_filter(filter_two)
    filter_two.set_filter(filter_three)

    ma0_records = filter_one.get_records()

    filter_visual = simulation_filters.NowDataFilter()
    filter_visual.set_records(ma0_records)
    datavisuallib.show_scatter("ici", "ibt", filter_visual.get_records())

    ma0_records = generate_json_records(ma0_records)
    save_records("D:\\Temp_data\\ma0_records.json",ma0_records)
    print(ma0_records)

    """
    10mA 部分
    """
    # init filters
    filter_one = simulation_filters.TenMaFilter()
    filter_two = simulation_filters.C34RecordsFilter()
    filter_three = simulation_filters.TenMaGenFilter()
    
    # set input records
    filter_one.set_records(records)
    # chain filters
    filter_one.set_filter(filter_two)
    filter_two.set_filter(filter_three)

    ma10_records = filter_one.get_records()

    filter_visual = simulation_filters.NowDataFilter()
    filter_visual.set_records(ma10_records)
    datavisuallib.show_scatter("itt", "ibt", filter_visual.get_records())

    ma10_records = generate_json_records(ma10_records)
    save_records("D:\\Temp_data\\ma10_records.json",ma10_records)
    print(ma10_records)

    """
    20mA 部分
    """
    # init filters
    filter_one = simulation_filters.TwentyMaFilter()
    filter_two = simulation_filters.C34RecordsFilter()
    filter_three = simulation_filters.TwentyMaGenFilter()
    
    # set input records
    filter_one.set_records(records)
    # chain filters
    filter_one.set_filter(filter_two)
    filter_two.set_filter(filter_three)

    ma20_records = filter_one.get_records()

    filter_visual = simulation_filters.NowDataFilter()
    filter_visual.set_records(ma20_records)
    datavisuallib.show_scatter("itt", "ibt", filter_visual.get_records())
  
    ma20_records = generate_json_records(ma20_records)
    save_records("D:\\Temp_data\\ma20_records.json",ma20_records)
    print(ma20_records)

    """
    30mA 部分
    """
    # init filters
    filter_one = simulation_filters.ThirtyMaFilter()
    filter_two = simulation_filters.C34RecordsFilter()
    filter_three = simulation_filters.ThirtyMaGenFilter()
    
    # set input records
    filter_one.set_records(records)
    # chain filters
    filter_one.set_filter(filter_two)
    filter_two.set_filter(filter_three)

    ma30_records = filter_one.get_records()

    filter_visual = simulation_filters.NowDataFilter()
    filter_visual.set_records(ma30_records)
    datavisuallib.show_scatter("itt", "ibt", filter_visual.get_records())

    ma30_records = generate_json_records(ma30_records)
    save_records("D:\\Temp_data\\ma30_records.json",ma30_records)
    print(ma30_records)

if __name__ == "__main__":
    main()