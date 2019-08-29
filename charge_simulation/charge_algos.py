import simulation_framework

"""
在此声明充电算法，所有算法类均应继承simulation_framework.ChargeAlgo
"""

class DemoAlgo(simulation_framework.ChargeAlgo):
    """
    样例类，提供一个超温停止充电120s的简单算法
    """
    def __init__(self):
        self.__ibt = 0
        self.__itt = 0
        self.__wait_seconds = 0

    def update(self, data_dict):
        self.__ibt = data_dict["ibt"]
        self.__itt = data_dict["itt"]

    def get_result(self):
        # if still waiting, update waiting timer
        if self.__wait_seconds > 0:
            self.__wait_seconds -= 2
            return {"ici": 0}
        # if over-heat, stop charing for 2mins
        elif self.__itt >= 390 or self.__ibt >= 390:
            self.__wait_seconds = 120
            return {"ici": 0}
        # else charge in 30.0mA
        else:
            return {"ici": 300}