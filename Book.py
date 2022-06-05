class Client:
    def __init__(self, id, title, description, author, status):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author
        self.__status = status

    def set_id(self, id):
        self.__id = id

    def set_full_name(self, title):
        self.__title = title

    def set_age(self, description):
        self.__description = description

    def set_id_no(self, author):
        self.__author = author

    def set_phone_number(self, status):
        self.__status = status

    def get_id(self):
        return self.__id

    def get_full_name(self):
        return self.__title

    def get_age(self):
        return self.__description

    def get_id_no(self):
        return self.__author

    def get_phone_number(self):
        return self.__status

