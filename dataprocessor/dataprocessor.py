# Data Processor by Krystian Ayala
# 
# This is a simple data processor to go with a given data file in a simple format. It takes in information about employees and returns them in a newer format that is much simpler to understand.
# The data is fed through the process_lines() method and the values are corrected if needed to match a specific format. 
# Afterwards, that information is put into a .pickle file and read back through and displayed to confirm it works as intended. 

import sys, pathlib, re, pickle

class Person:
    # __init__ method to fields that each person should have.
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    # display method to properly display employees and their information.
    def display(self):
        print("\nEmployee id: " + self.id)
        print("\t\t" + self.first + " " + self.mi + " " + self.last)
        print("\t\t" + self.phone)


# The lines from the data.csv get processed here.
def process_lines(text):
    '''
      Processes lines given from the data.csv file in a specific format and updates the values to match a specific format.
      Args:
        text: a list of strings to be processed and adjusted if necessary
      Returns: dict of Person objects
        employee_dict: a dict of Person objects with the employee ID being the key value
    '''

    # employee_dict serves as a dict of Person objects that will be updated and returned at the end of the method.
    employee_dict = {}

    # The data is processed line by line in this for loop.
    for i in text:
        # Grabbing a line of employee info and separating it into parts for easier processing.
        employee = i.split(",")

        # Last name is set into its own variable then capitilizes the first letter in the name as well as making sure
        # the rest of the name is lowercase.
        last_name = employee[0]
        last_name = last_name[0].upper() + last_name[1:].lower()

        # First name is set into its own variable then capitilizes the first letter in the name as well as making sure
        # the rest of the name is lowercase.
        first_name = employee[1]
        first_name = first_name[0].upper() + first_name[1:].lower()

        # Initial is set into its own variable and is then capitalized. If there is no initial, then X is put in place.
        initial = employee[2].upper()
        if not initial:
            initial = "X"

        # ID is given a variable and regex is used to determine if ID matches the required format, prompts user for a
        # new ID if it doesn't meet the criteria.
        id = employee[3]
        if not re.match(r"^[A-Z]{2}[0-9]{4}$", id):
            print("ID invalid: " + id)
            print("ID is two letters followed by 4 digits")
            id = input("Please enter a valid id: ")

        # The phone number is stored in a var and non-numerical characters are replaced with "-" using regex
        phone = re.sub(r"\D", "-", employee[4])
        # If the length of the 10-digit phone number (plus 2 hypens) is less than twelve, then hyphens are added in.
        if len(phone) < 12:
            phone = phone[0:3] + "-" + phone[3:6] + "-" + phone[6:]

        # A simple check to determine if there's a duplicate key value within employee_dict
        if id in employee_dict:
            print("ERROR: duplicate ID detected in data.csv file")

        # Adds new key using employee ID and the value is a Person object containing the employee's information when
        # finished with fixing/formatting everything.
        employee_dict[id] = Person(last_name, first_name, initial, id, phone)

    return employee_dict


# This whole section of code is responsible for getting the correct file path, obtaining data
# from data.csv and processing it, and pickling the employees info.
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter a filename as a system arg")
        quit()

    # Finding path to data file through the given path in sysarg
    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), "r") as f:
        text_in = f.read().splitlines()

    # Employees get processed through the process_lines() method.
    employees = process_lines(text_in[1:]) # Ignores heading line

    # Pickle the employees
    pickle.dump(employees, open("employees.pickle", "wb"))

    # Read the pickle back in
    employees_in = pickle.load(open("employees.pickle", "rb"))

    # Output employees
    print("\n\nEmployee list: ")
    # Looks up all the keys in the employees_in dict based off employee ID's.
    for emp_id in employees_in.keys():
        employees_in[emp_id].display() # Uses the display() method from the Person class to show employees and their information.
