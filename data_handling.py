import abc
import re

"""
以下定义抽象类
"""
# DataHandler类，用于对源文件的数据读入和处理
# 用户不应直接操作本类
class DataHandler(metaclass = abc.ABCMeta):
    # public 读入源文件数据方法
    # return: none
    @abc.abstractclassmethod
    def read_data(self, filename):
        pass
    
    # public 处理读入数据方法
    # return: none
    @abc.abstractclassmethod
    def process_data(self):
        pass

    # public 取得源文件数据方法
    # return: list
    @abc.abstractclassmethod
    def show_data(self):
        pass


# DataIterator类，用于提供多个DataHandler取得数据的迭代器
# 用户不应直接操作本类
class DataIterator(metaclass = abc.ABCMeta):
    # public 读入新数据
    # return: none
    @abc.abstractclassmethod
    def add_data_handler(self, filename):
        pass

    # public 返回数据迭代器
    @abc.abstractclassmethod
    def show_all_data(self):
        pass

"""
以下为工厂方法模式的工厂与产品抽象类
"""
class DataIteratorCreator(metaclass = abc.ABCMeta):
    # public 读入新数据
    # return: none
    @abc.abstractclassmethod
    def create_iterator(self):
        pass

class Creator(metaclass = abc.ABCMeta):
    # input DataIterator obj
    # return: Product
    @abc.abstractclassmethod
    def create_product(self, iterator):
        pass


class Product(metaclass = abc.ABCMeta):
    # input DataIterator obj
    @abc.abstractclassmethod
    def __init__(self, itertor):
        pass

    # public 在产品类对象内部初始化DataIterator对象
    @abc.abstractclassmethod
    def read_data(self, filename):
        pass

    # public 处理数据
    @abc.abstractclassmethod
    def process_data(self):
        pass

    # public 返回数据
    @abc.abstractclassmethod
    def show_result(self):
        pass


"""
以下为具体实现类
"""
class IPGDataGetter(DataHandler):
    __re_pattern = re.compile("[0-9]+")
    
    def __init__(self):
        self.__file_data = list()
        self.__processed_file_data = list()
        self.__has_hk = False

    # public 读入源文件数据方法
    # return: none
    def read_data(self, filename):
        file_obj = open(filename, "r", encoding="ISO-8859-15")
        for line in file_obj.readlines():
            self.__file_data.append(line)
        file_obj.close()
    
    # protected 确认某行是否为合理数据
    # return boolean
    """
    hk 后的第一条数据不准，在此过滤 --2019.08.29
    """
    def _is_valid_line(self, line):
        line_elements = line.split()
        if len(line_elements) == 23 and line_elements[0] == "IPG:":
            if self.__has_hk:
                #print("abondoning")
                self.__has_hk = False
                return False
            else:
                return True
        elif "hk" in line_elements:
            #print("hk")
            self.__has_hk = True
            return False
        else:
            return False

    def _split_line(self, line):
        elements = self.__re_pattern.findall(line)
        # [icv, ici, ibv, ibt, itt, freq, temp_th, tick]
        needed_elements = elements[0:4] + elements[5:6] + elements[7:9] + elements[-1:]
        return needed_elements
        

    # public 处理读入数据方法
    # return: none
    def process_data(self):
        for line in self.__file_data:
            if self._is_valid_line(line):
                self.__processed_file_data.append(self._split_line(line))

    # public 取得源文件数据方法
    # return: list
    def show_data(self):
        return self.__processed_file_data


class IPGDataIterator(DataIterator):
    def __init__(self):
        self.__processed_file_data = list()

    # public 读入新数据
    # return: none
    def add_data_handler(self, filename):
        data_handler = IPGDataGetter()
        data_handler.read_data(filename)
        data_handler.process_data()
        self.__processed_file_data = data_handler.show_data()

    # public 返回数据迭代器
    def show_all_data(self):
        for line in self.__processed_file_data:
            yield line


class IPGDataIteratorFactory(DataIteratorCreator):
    def create_iterator(self):
        return IPGDataIterator()

"""
返回完整记录的处理类
(icv, ici, ibv, ibt, itt, freq, temp_th, tick)
"""
class NoFilterProduct(Product):
    def __init__(self, iterator):
        self.__data_iterator = iterator
        self.__processed_data = list()

    # public 在产品类对象内部创建一个DataIterator对象
    def read_data(self, filename):
        self.__data_iterator.add_data_handler(filename)

    # public 处理数据
    def process_data(self):
        for line in (self.__data_iterator).show_all_data():
            self.__processed_data.append(line)

    # public 返回数据
    def show_result(self):
        for line in self.__processed_data:
            # (icv, ici, ibv, ibt, itt, freq, temp_th, tick)
            yield tuple(line)
            

class NoFilterFactory(Creator):
    def create_product(self, iterator):
        return NoFilterProduct(iterator)


"""
返回间隔两秒的记录组的处理类
((icv, ici, ibv, ibt, itt, freq, temp_th, tick), (ibt, itt, temp_th))
"""
class SecondFilterProduct(Product):
    def __init__(self, iterator):
        self.__data_iterator = iterator
        self.__processed_data = list()

    # public 在产品类对象内部创建一个DataIterator对象
    def read_data(self, filename):
        self.__data_iterator.add_data_handler(filename)

    def _get_now_data(self, elements):
        return tuple(elements[:-1])

    def _get_then_data(self, elements):
        return tuple(elements[3:5] + elements[6:7])

    # public 处理数据
    def process_data(self):
        temp_data = list()
        for line in (self.__data_iterator).show_all_data():
            temp_data.append(line)
        for i in range(len(temp_data) - 1):
            tick_now = int(temp_data[i][-1])
            tick_then = int(temp_data[i+1][-1])
            if tick_now == tick_then - 2:
                self.__processed_data.append((self._get_now_data(temp_data[i]), self._get_then_data(temp_data[i+1])))

    # public 返回数据
    def show_result(self):
        for line in self.__processed_data:
            # [icv, ici, ibv, ibt, itt, freq, temp_th, tick]
            yield tuple(line)
            

class SecondFilterFactory(Creator):
    def create_product(self, iterator):
        return SecondFilterProduct(iterator)