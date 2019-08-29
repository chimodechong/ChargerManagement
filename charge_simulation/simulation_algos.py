import simulation_framework
import recordslib
import sys

class ConcreteSandbox(simulation_framework.SimulationSandBox):
    def __init__(self):
        self.__chg_algo = None
        self.__simu_algo = None
        self.__simu_results = []
        self.__current_data = dict()
        self.__tick = 0

    def set_init_data(self, data_dict):
        self.__current_data = data_dict

    def add_charge_algo(self, algo_obj):
        self.__chg_algo = algo_obj

    def add_simu_algo(self, algo_obj):
        self.__simu_algo = algo_obj

    def one_step(self):
        # now current_data contains the current temp and the ici before
        self.__chg_algo.update(self.__current_data)
        self.__current_data.update(self.__chg_algo.get_result())
        # now current_data contains the current temp and the ici
        # add data dict to list
        self.__current_data.update({"tick":self.__tick})
        new_data = dict()
        new_data.update(self.__current_data)
        self.__simu_results.append(new_data)
        # use the data now to calculate next environment
        self.__tick += 2
        self.__simu_algo.set_data(self.__current_data)
        self.__current_data.update(self.__simu_algo.get_result())

    def seconds_simu(self, seconds):
        while seconds > 0:
            self.one_step()
            seconds -= 2

    def get_simu_data(self):
        return self.__simu_results


class ConcreteSimuAlgo(simulation_framework.SimulationAlgo):
    def __init__(self):
        self.__0ma_dataset = None
        self.__10ma_dataset = None
        self.__20ma_dataset = None
        self.__30ma_dataset = None
        self.__current_data = None

    def set_data_set(self, data_set):
        """
        for each dataset
        dict{ { (ibt*1000 + itt): dict{ (ibt_then*1000 + itt_then): num_of_appearance } }
        """
        self.__0ma_dataset = data_set[0]
        self.__10ma_dataset = data_set[1]
        self.__20ma_dataset = data_set[2]
        self.__30ma_dataset = data_set[3]

    def set_data(self, data):
        self.__current_data = data

    def get_result(self):
        data_key = str(int(self.__current_data["ibt"] * 1000 + self.__current_data["itt"]))
        if self.__current_data["ici"] == 0:
            result = int(recordslib.record_change(self.__0ma_dataset[data_key]))
        elif self.__current_data["ici"] == 100:
            result = int(recordslib.record_change(self.__10ma_dataset[data_key]))
        elif self.__current_data["ici"] == 200:
            result = int(recordslib.record_change(self.__20ma_dataset[data_key]))
        elif self.__current_data["ici"] == 300:
            result = int(recordslib.record_change(self.__30ma_dataset[data_key]))
        else:
            print("ici out of range")
            sys.exit(-1)
        return {"ibt": ((result - (result%1000))/1000), "itt" : (result%1000)}