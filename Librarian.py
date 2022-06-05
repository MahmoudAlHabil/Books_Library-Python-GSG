class Librarian:
    def __init__(self, id, full_name, age, id_no, employment_type):
        self.__id = id
        self.__full_name = full_name
        self.__age = age
        self.__id_no = id_no
        self.__employment_type = employment_type

    def set_id(self, id):
        self.__id = id

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def set_age(self, age):
        self.__age = age

    def set_id_no(self, id_no):
        self.__id_no = id_no

    def set_phone_number(self, employment_type):
        self.__employment_type = employment_type

    def get_id(self):
        return self.__id

    def get_full_name(self):
        return self.__full_name

    def get_age(self):
        return self.__age

    def get_id_no(self):
        return self.__id_no

    def get_phone_number(self):
        return self.__employment_type

