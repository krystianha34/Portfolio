# Data Processor
The two files to run this program are located here: 
[Data Processor](dataprocessor.py) and [Data File](data.csv)

A simple program in Python to take an input file using sysarg and correct errors in formatting. It will prompt the user to fix the mistakes if any, then adds these values into a dictionary. 

The example uses sample employee information. Given a last and first name, middle initial, employee id, and a phone number. They are formatted in a uniform way and if there's an error, then the user is prompted to fix it by inputting a new value. 

Finally, the information is put into a dictionary and turned into a .pickle file. The program reads the .pickle file back and displays the employee information so the user can confirm everything is correct. 
