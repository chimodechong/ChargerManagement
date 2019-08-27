@startuml
Object Creator
Creator : +create_product()

Object Product
Product : +read_data()
Product : -process_data()
Product : +show_result()

Object DataHandler
DataHandler : +read_data()
DataHandler : +process_data()
DataHandler : +show_data()

Object DataIterator
DataIterator : +add_data_handler()
DataIterator : +show_all_data()

Object ConcreteCreatorA
ConcreteCreatorA : +create_product()

Object ConcreteCreatorB
ConcreteCreatorB : +create_product()

Object ConcreteProductA
ConcreteProductA : -data_iterator
ConcreteProductA : -processed_data
ConcreteProductA : +process_data()
ConcreteProductA : +show_result()

Object ConcreteProductB
ConcreteProductB : -data_iterator
ConcreteProductB : -processed_data
ConcreteProductB : +process_data()
ConcreteProductB : +show_result()

Object ConcreteDataHandler
ConcreteDataHandler : -file_data
ConcreteDataHandler : -processed_file_data
ConcreteDataHandler : +read_data()
ConcreteDataHandler : +process_data()
ConcreteDataHandler : +show_data()

Object ConcreteDataIterator
ConcreteDataIterator : -data_handler_list
ConcreteDataIterator : +add_data_handler()
ConcreteDataIterator : +show_all_data()

Product <|-- ConcreteProductA
Creator <|-- ConcreteCreatorA
Product <|-- ConcreteProductB
Creator <|-- ConcreteCreatorB
DataHandler <|-- ConcreteDataHandler
DataIterator <|-- ConcreteDataIterator
ConcreteProductA <.. ConcreteCreatorA
ConcreteProductB <.. ConcreteCreatorB
ConcreteDataIterator o-- ConcreteDataHandler
ConcreteProductA *--> DataIterator
ConcreteProductB *--> DataIterator
@enduml