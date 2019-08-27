import abc

"""
定义抽象类，实际类应在simulation_filters, simulation_algos, charge_algos分别定义
"""
class DataFilter(metaclass = abc.ABCMeta):
    @abc.abstractclassmethod
    def __init__(self):
        pass

    @abc.abstractclassmethod
    def set_filter(self, filter):
        pass

    @abc.abstractclassmethod
    def set_records(self, records):
        pass

    @abc.abstractclassmethod
    def _process_records(self):
        pass

    @abc.abstractclassmethod
    def get_records(self):
        pass