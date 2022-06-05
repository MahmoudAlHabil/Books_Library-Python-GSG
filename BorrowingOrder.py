class Client:
    def __init__(self, id, date, client_id, book_id, status):
        self.__id = id
        self.__date = date
        self.__client_id = client_id
        self.__book_id = book_id
        self.__status = status

    def set_id(self, id):
        self.__id = id

    def set_full_name(self, date):
        self.__date = date

    def set_age(self, client_id):
        self.__client_id = client_id

    def set_id_no(self, book_id):
        self.__book_id = book_id

    def set_phone_number(self, status):
        self.__status = status

    def get_id(self):
        return self.__id

    def get_full_name(self):
        return self.__date

    def get_age(self):
        return self.__client_id

    def get_id_no(self):
        return self.__book_id

    def get_phone_number(self):
        return self.__status
