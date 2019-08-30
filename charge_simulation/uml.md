@startuml
abstract class DataFilter {
    {abstract} __init__()
    {abstract} set_filter()
    {abstract} set_records()
    {abstract} _process_records()
    {abstract} get_records()
}

class ConcreteDataFilter {
    +_process_records()
}

abstract class ChargeAlgo {
    {abstract} __init__()
    {abstract} update()
    {abstract} get_result()
}

class ConcreteChargeAlgo {
    +__init__()
    +update()
    +get_result()
}

abstract class SimulationAlgo {
    {abstract} set_data_set()
    {abstract} set_data()
    {abstract} get_result()
}

class ConcreteSimulationAlgo {
    +__init__()
    +set_data_set()
    +set_data()
    +get_result()
}

abstract class SimulationSandBox {
    {abstract} set_init_data()
    {abstract} add_charge_algo()
    {abstract} add_simu_algo()
    {abstract} one_step()
    {abstract} get_simu_data()
}

class ConcreteSandBox {
    +__init__()
    +set_init_data()
    +add_charge_algo()
    +add_simu_algo()
    +one_step()
    +get_simu_data()
}

DataFilter o--> DataFilter
DataFilter<|--ConcreteDataFilter
SimulationSandBox<|--ConcreteSandBox
SimulationAlgo<|--ConcreteSimulationAlgo
ChargeAlgo<|--ConcreteChargeAlgo
ConcreteSandBox --> SimulationAlgo
ConcreteSandBox --> ChargeAlgo
@enduml