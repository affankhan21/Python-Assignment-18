"""2. WAP a menu driven program to perform following operations using 
files :
a. Add a record
b. Search for a record using id
c. Delete a record using id
d. Edit a record using id.
e. Display all records"""

from empmgmt import EmpMgmt
import os

if(__name__ =="__main__"):
   obj = EmpMgmt()
   ch =0

   if os.path.exists("emp.txt"):
       obj.allEmp = obj.deserialization()

   while(ch!=6):
        print("\nMenu:")
        print("1. Add a record")
        print("2. Search for a record")
        print("3. Delete a record")
        print("4. Edit a record")
        print("5. Display all records")
        print("6. Exit")
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            obj.add_record()
            
        elif choice == 2:
            id = int(input("Enter id you want to search: "))
            obj.search_record(id)
        elif choice == 3:
            id = int(input("Enter id you want to delete: "))
            obj.delete_record(id)
            
        elif choice == 4:
            id = int(input("Enter id you want to Edit: "))
            obj.edit_record(id)
        elif choice == 5:
            obj.display_all_records()
        elif choice == 6:
            obj.serialization()
            break
