from Client import Client
from Librarian import Librarian


def main():
    print("Hello World!")
    client = Client(1, "John Doe", 20, "123456789", "0712345678")
    print(client.get_id())
    client.set_full_name('mahmoud alhabil')
    print(client.get_full_name())

    clients = []
    librarians = []
    books = []
    borrowed_orders = []
    total_borrowed_books = len(borrowed_orders)
    total_available_books = len(books) - len(borrowed_orders)
    total_borrowed_orders = len(borrowed_orders)

    print(total_borrowed_orders, total_borrowed_books, total_available_books)

    clients.append(Client(1, 'Mahmoud AlHabil', 21, '407048305', '0592773665'))
    print(len(clients))

    librarians.append(Librarian(1, 'Ahmed Ali', 27, '404040404', '0591234567'))
    print(len(librarians))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
