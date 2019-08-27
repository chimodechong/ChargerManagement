import simulation_filters
import recordslib

def main():
    print("starting program")
    records = recordslib.get_json_records("D:/Temp_data/results.json")
    print("records got")

    """
    将filter串联以逐级过滤数据
    """
    # init filters
    filter_one = simulation_filters.TenMaFilter()
    filter_two = simulation_filters.TopTenDiffRecordsFilter()
    filter_three = simulation_filters.TempDataFilter()
    # set input records
    filter_one.set_records(records)
    # chain filters
    filter_one.set_filter(filter_two)
    filter_two.set_filter(filter_three)
    # get result from the head filter
    recordslib.print_records(filter_one.get_records())

if __name__ == "__main__":
    main()