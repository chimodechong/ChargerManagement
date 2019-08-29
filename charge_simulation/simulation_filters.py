import simulation_framework
import operator

class ModelFilter(simulation_framework.DataFilter):
    """
    所有filter的基类, 继承后应只修改_process_records()方法
    _ori_records: 存放传入的记录
    _processed_records: 存放处理好的记录
    """
    def __init__(self):
        self._ori_records = []
        self._processed_records = []
        self._next_filter = None

    def set_filter(self, filter):
        self._next_filter = filter

    def set_records(self, records):
        self._ori_records = records

    def _process_records(self):
        pass

    def get_records(self):
        self._process_records()
        if self._next_filter == None:
            return self._processed_records
        else:
            self._next_filter.set_records(self._processed_records)
            return self._next_filter.get_records()


class ZeroMaFilter(ModelFilter):
    # records should contain [ici] at least
    def _process_records(self):
        for record in self._ori_records:
            if record[0]["ici"] <= 20:
                self._processed_records.append(record)


class ZeroMaGenFilter(ModelFilter):
    """
    change all ici to 0
    """
    # records should contain [ici] at least
    def _process_records(self):
        for record in self._ori_records:
            new_record = [dict(), dict()]
            new_record[0].update(record[0])
            new_record[1].update(record[1])
            new_record[0].update({"ici":0})
            self._processed_records.append(new_record)


class TenMaFilter(ModelFilter):
    # records should contain [ici] at least
    def _process_records(self):
        for record in self._ori_records:
            if record[0]["ici"] >= 80 and record[0]["ici"] <= 120:
                self._processed_records.append(record)


class TenMaGenFilter(ModelFilter):
    """
    change all ici to 100
    """
    # records should contain [ici] at least
    def _process_records(self):
        for record in self._ori_records:
            new_record = [dict(), dict()]
            new_record[0].update(record[0])
            new_record[1].update(record[1])
            new_record[0].update({"ici":100})
            self._processed_records.append(new_record)


class TwentyMaFilter(ModelFilter):
    # records should contain [ici] at least
    def _process_records(self):
        for record in self._ori_records:
            if record[0]["ici"] >= 180 and record[0]["ici"] <= 220:
                self._processed_records.append(record)


class TwentyMaGenFilter(ModelFilter):
    """
    change all ici to 200
    """
    # records should contain [ici] at least
    def _process_records(self):
        for record in self._ori_records:
            new_record = [dict(), dict()]
            new_record[0].update(record[0])
            new_record[1].update(record[1])
            new_record[0].update({"ici":200})
            self._processed_records.append(new_record)


class ThirtyMaFilter(ModelFilter):
    # records should contain [ici] at least
    def _process_records(self):
        for record in self._ori_records:
            if record[0]["ici"] >= 280 and record[0]["ici"] <= 320:
                self._processed_records.append(record)


class ThirtyMaGenFilter(ModelFilter):
    """
    change all ici to 300
    """
    # records should contain [ici] at least
    def _process_records(self):
        for record in self._ori_records:
            new_record = [dict(), dict()]
            new_record[0].update(record[0])
            new_record[1].update(record[1])
            new_record[0].update({"ici":300})
            self._processed_records.append(new_record)


class TempDataFilter(ModelFilter):
    """
    将数据过滤为[{"ici", "ibt", "itt"},{"ibt", "itt"}]
    传入的数据应确保至少包含这数项
    !!!---------------类自身不检查传入数据正确性---------------!!!
    """
    def _process_records(self):
        for record in self._ori_records:
            new_record = [dict(), dict()]
            new_record[0]["ici"] = record[0]["ici"]
            new_record[0]["ibt"] = record[0]["ibt"]
            new_record[0]["itt"] = record[0]["itt"]
            new_record[1]["ibt"] = record[0]["ibt"]
            new_record[1]["itt"] = record[0]["itt"]
            self._processed_records.append(new_record)


class TopTenRecordsFilter(ModelFilter):
    def _process_records(self):
        for record in self._ori_records:
            #print(record)
            if len(self._processed_records) > 10:
                break
            self._processed_records.append(record)


class TopHundredRecordsFilter(ModelFilter):
    def _process_records(self):
        for record in self._ori_records:
            #print(record)
            if len(self._processed_records) > 100:
                break
            self._processed_records.append(record)


class TopThousandRecordsFilter(ModelFilter):
    def _process_records(self):
        for record in self._ori_records:
            #print(record)
            if len(self._processed_records) > 1000:
                break
            self._processed_records.append(record)


class TopTenDiffRecordsFilter(ModelFilter):
    def _process_records(self):
        previous_record = [dict(),dict()]
        for record in self._ori_records:
            if len(self._processed_records) > 10:
                break
            try:
                differ1 = set(record[0].items()) ^ set(previous_record[0].items())
                differ2 = set(record[1].items()) ^ set(previous_record[1].items())
                if len(differ1) == 0 and len(differ2) == 0:
                    continue
            except:
                pass
            if len(previous_record) == 0:
                previous_record = record    
            self._processed_records.append(record)


class C34RecordsFilter(ModelFilter):
    def _process_records(self):
        for record in self._ori_records:
            if record[0]["ibt"] >= 340 and record[0]["itt"] >= 340:
                self._processed_records.append(record)

class NowDataFilter(ModelFilter):
    """
    this class returns [{dict}, {}, {}...]
    each dict is a "now" data deprived from the original [{now_data}, {then_data}]
    """
    def _process_records(self):
        for record in self._ori_records:
            self._processed_records.append(record[0])
