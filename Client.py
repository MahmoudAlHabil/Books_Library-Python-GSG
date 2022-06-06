from User import User


class Client(User):
    def __init__(self, id, full_name, age, id_no, phone_number):
        super().__init__(id, full_name, age, id_no)
        self.__phone_number = phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number

