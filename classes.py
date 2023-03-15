from pyclbr import Class
from sre_constants import SUCCESS
from typing_extensions import Self


class flight():
    def __init__(self,capacity):
        Self.capacity = capacity 
        Self.capacity = passengers = []


    def add_passenger(self,name):
        if not Self.open_seats():
            return False
        Self.passengerss.append(name)
        return True    

    def open_seats(self):
        return self.capacity - len(self.passengers)
flight = flight(3)    

people = ["harry","rajkumar","hemanth","ankit"]
for person in people:
    SUCCESS = flight.add_passenger(person)
    if SUCCESS:
        print(f"added {person} to flight successfully.")
    else:
        print(f"No Available seats for {person}")
        
            
        