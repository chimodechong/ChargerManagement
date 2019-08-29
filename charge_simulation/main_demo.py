import simulation_algos
import charge_algos
import datavisuallib
import recordslib
import datavisuallib

def main():
    ma0_records = recordslib.get_json_records("D:\\Temp_data\\ma0_records.json")
    ma10_records = recordslib.get_json_records("D:\\Temp_data\\ma10_records.json")
    ma20_records = recordslib.get_json_records("D:\\Temp_data\\ma20_records.json")
    ma30_records = recordslib.get_json_records("D:\\Temp_data\\ma30_records.json")

    simu_sandbox = simulation_algos.ConcreteSandbox()
    simu_algo = simulation_algos.ConcreteSimuAlgo()
    chg_algo = charge_algos.DemoAlgo()

    simu_algo.set_data_set((ma0_records, ma10_records, ma20_records, ma30_records))
    simu_sandbox.add_charge_algo(chg_algo)
    simu_sandbox.add_simu_algo(simu_algo)
    simu_sandbox.set_init_data({"ibt":350, "itt":350})

    simu_sandbox.seconds_simu(9600)
    results = simu_sandbox.get_simu_data()
    """
    datavisuallib.show_figure("tick", "ibt", results)
    datavisuallib.show_figure("tick", "itt", results)
    datavisuallib.show_figure("tick", "ici", results)
    """
    datavisuallib.show_charge_process(results)

if __name__ == "__main__":
    main()