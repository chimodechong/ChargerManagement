import simulation_framework


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


class TenMaFilter(ModelFilter):
    # records should contain [ici] at least
    def _process_records(self):
        for record in self._ori_records:
            if record[0]["ici"] >= 70 and record[0]["ici"] <= 130:
                self._processed_records.append(record)


class TwentyMaFilter(ModelFilter):
    # records should contain [ici] at least
    def _process_records(self):
        for record in self._ori_records:
            if record[0]["ici"] >= 170 and record[0]["ici"] <= 230:
                self._processed_records.append(record)


class ThirtyMaFilter(ModelFilter):
    # records should contain [ici] at least
    def _process_records(self):
        for record in self._ori_records:
            if record[0]["ici"] >= 270 and record[0]["ici"] <= 330:
                self._processed_records.append(record)


class TempDataFilter(ModelFilter):
    """
    将数据过滤为[{"ici", "ibt", "itt"},{"ibt", "itt"}]
    传入的数据应确保至少包含这数项
    !!!---------------类自身不检查传入数据正确性---------------!!!
    """
    def _process_records(self):
        new_record = [dict(), dict()]
        for record in self._ori_records:
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