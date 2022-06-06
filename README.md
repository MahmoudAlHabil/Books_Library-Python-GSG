# Books_Library-Python-GSG
Final project for IT and coding foundations course - GSG
 
Books Library 
You have to design a system for borrowing books from a library: 

Requirements: 

  ● Client 
  
    ○ Properties: 
    
      ■ id 
      ■ full_name 
      ■ age 
      ■ id_no 
      ■ phone_number 
      
  ● Librarian 
  
    ○ Properties: 
    
      ■ id 
      ■ full_name 
      ■ age 
      ■ id_no 
      ■ emplyment_type(Full/part) 
      
  ● Book 
  
    ○ Properties: 
    
      ■ id 
      ■ title 
      ■ description 
      ■ author 
      ■ status(Active-Inactive) 
      
  ● Borrowing Order: 
  
    ○ Properties: 
    
      ■ id 
      ■ date 
      ■ client_id 
      ■ book_id 
      ■ status (Active - Expired - Cancelled) 
      
  ● Main File 
  
    ○ Properties: 
    
      ■ list of clients 
      ■ list of librarians 
      ■ list of books 
      ■ list of borrowed_orders 
      ■ total_borrowed_books 
      ■ total_available_books 
      ■ total_borrowed_orders
      
    
Scenario: 
1. Create a new client and add it to the client's list. 
2. Create a new librarian and add it to the librarian’s list. 
3. Create more than 3 books and add them to the book’s list. 
4. Ask Librarian to borrow a book 
5. The librarian will ask you which book you want to borrow. 
6. Checkbook status, Check if the box is active for borrowing or not, 7. if active the librarian will ask you about your information (id_no) 
8. The librarian will check if the client exists in the system or not. 
9. if it exists the librarian will create a borrow_order with the selected book and the selected client 
10. Return book to librarian will be like that the client enters borrowing_id to the librarian to return it.

