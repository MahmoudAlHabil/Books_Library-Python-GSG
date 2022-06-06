from User import User


class Librarian(User):
    def __init__(self, id, full_name, age, id_no, employment_type):
        super().__init__(id, full_name, age, id_no)
        self.__employment_type = employment_type

    def set_employment_type(self, employment_type):
        self.__employment_type = employment_type

    def get_employment_type(self):
        return self.__employment_type

