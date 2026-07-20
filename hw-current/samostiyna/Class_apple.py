from Class_laptop import *

class Apple(Laptop):
    def __init__(self, brand, screen_size, price, ram, model, processor):
        super().__init__(brand,screen_size,price,ram)
        self.__model = self.__validate_model(model)
        self.__processor = self.__validate_processor(processor)


    @property
    def model(self):
        return self.__model

    @property
    def processor(self):
        return self.__processor


    def __validate_model(self,value):
        if not isinstance(value,str):
            raise TypeError("Model must be a string")
        return value

    def __validate_processor(self,value):
        if not isinstance(value,str):
            raise TypeError("Processor must be a string")
        return value

    def __str__(self):
        return f"|{super().__str__()[1:-1]}|{self.__model} |{self.__processor} |"

