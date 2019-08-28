import abc

"""
定义抽象类，实际类应在simulation_filters, simulation_algos, charge_algos分别定义
"""
class DataFilter(metaclass = abc.ABCMeta):
    """
    数据过滤器抽象类
    """
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


class ChargeAlgo(metaclass = abc.ABCMeta):
    """
    算法抽象类，应提供数据初始化，更新数据，获得结果接口
    ChargeAlgo.update ---> get_result ---> update ---> get_result ----> update ---> ...
    """
    @abc.abstractclassmethod
    def __init__(self):
        """
        仅为声明非静态属性，不赋予属性有意义初始值
        """
        pass
    
    @abc.abstractclassmethod
    def update(self, data_dict):
        pass

    @abc.abstractclassmethod
    def get_result(self):
        pass