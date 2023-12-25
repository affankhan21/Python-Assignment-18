from Ass1 import Employee
import pickle

class EmpMgmt:
    def __init__(self):
        self.allEmp = []
    
    def add_record(self):
        eid = int(input("Enter the id: "))
        ename = input("Enter the name: ")
        salary = float(input("Enter the salary: "))
        a1 = Employee(eid, ename, salary)
        self.allEmp.append(a1)
    
    def search_record(self,id):
        for e in self.allEmp:
            if id == e.id:
                print("Employee Found")
                print(e)
                break
        else:
            print("Employee Not found")
    
    def delete_record(self,id):
        for e in  self.allEmp:
            if id == e.id:
                print("Employee found")
                self.allEmp.remove(e)
                break
        else:
            print("No such employee is present.")
    
    def edit_record(self,id):
        for e in self.allEmp:
            if id == e.id:
                print("Employee Found ")
                name = input("Enter new Name: ")
                salary = int(input("Enter New Salary: "))
                e.name = name
                e.salary = salary
                print("Record Updated Successfully!")
                break
        else:
            print("Employee not found")

    def display_all_records(self):
            for e in self.allEmp:
                print(e)
    
    def serialization(self):
        with open("emp.txt", 'wb') as fp:
            pickle.dump(self.allEmp, fp)
    
    def deserialization(self):
        with open("emp.txt","rb") as fp:
            d1 = pickle.load(fp)
            return d1    

