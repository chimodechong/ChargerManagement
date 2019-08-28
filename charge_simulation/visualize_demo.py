import simulation_filters
import recordslib
import datavisuallib

def main():
    print("starting program")
    records = recordslib.get_json_records("D:/Temp_data/results.json")
    print("records got")

    # init filters
    filter_one = simulation_filters.NowDataFilter()
    # set input records
    filter_one.set_records(records)
    # chain filters

    # get result from the head filter
    datavisuallib.show_scatter("ibt", "itt", filter_one.get_records())

if __name__ == "__main__":
    main()