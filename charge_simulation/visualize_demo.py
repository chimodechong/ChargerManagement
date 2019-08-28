import simulation_filters
import recordslib
import datavisuallib

def main():
    print("starting program")
    records = recordslib.get_json_records("D:/Temp_data/results1.json") + recordslib.get_json_records("D:/Temp_data/results2.json")
    print(len(records), " records got")

    # init filters
    filter_one = simulation_filters.C34RecordsFilter()
    filter_two = simulation_filters.NowDataFilter()
    # set input records
    filter_one.set_records(records)
    # chain filters
    filter_one.set_filter(filter_two)
    # get result from the head filter
    datavisuallib.show_scatter("ibt", "itt", filter_one.get_records())

if __name__ == "__main__":
    main()