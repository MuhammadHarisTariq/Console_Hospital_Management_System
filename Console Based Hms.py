import os

# Function to add a new doctor record
def writeD():
    with open('DoctorPy.txt', 'a') as file:
        c = 'y'
        while c.lower() == 'y':
            # Get doctor details from the user
            id = input("Enter Doctor ID: ")
            name = input("Enter Doctor Name: ")
            age = input("Enter Doctor Age: ")
            mobile = input("Enter Doctor Mobile number: ")
            department = input("Enter Doctor work department: ")
            salary = input("Enter Doctor salary: ")
            # Write the details to the file
            file.write(f"{id}\t\t{name}\t\t{age}\t\t{mobile}\t\t{department}\t\t{salary}\n")
            c = input('Do you want to enter more records (y/n)? ')
    print('File saved successfully.')

# Function to read and display all doctor records
def readD():
    with open('DoctorPy.txt', 'r') as file:
        print('ID\t\tName\t\tAge\t\tMobile\t\tDepartment\t\tSalary')
        print('-' * 95)
        for line in file:
            print(line, end='')

# Function to search for a doctor by ID
def searchByIdD():
    c = 'y'
    while c.lower() == 'y':
        id = input('Enter Doctor ID to search: ')
        with open('DoctorPy.txt', 'r') as file:
            found = False
            for line in file:
                fields = line.split('\t\t')
                if fields[0] == id:
                    found = True
                    print('ID\t\tName\t\tAge\t\tMobile\t\tDepartment\t\tSalary')
                    print('-' * 95)
                    print(line)
                    break
            if not found:
                print('Doctor not found!')
        c = input('Do you want to search more Doctors (y/n)? ')

# Function to search for a doctor by Name
def searchByNameD():
    c = 'y'
    while c.lower() == 'y':
        name = input('Enter Doctor Name to search: ')
        with open('DoctorPy.txt', 'r') as file:
            found = False
            for line in file:
                fields = line.split('\t\t')
                if fields[1] == name:
                    found = True
                    print('ID\t\tName\t\tAge\t\tMobile\t\tDepartment\t\tSalary')
                    print('-' * 95)
                    print(line)
                    break
            if not found:
                print('Doctor not found!')
        c = input('Do you want to search more Doctors (y/n)? ')

# Function to update a doctor record by ID
def updateByIdD():
    c = 'y'
    while c.lower() == 'y':
        id = input('Enter Doctor ID to update: ')
        with open('DoctorPy.txt', 'r') as file:
            lines = file.readlines()

        with open('DoctorPy.txt', 'w') as file:
            found = False
            for line in lines:
                fields = line.split('\t\t')
                if fields[0] == id:
                    found = True
                    # Get new details from the user
                    id = input("Enter new Doctor ID: ")
                    name = input("Enter new Doctor Name: ")
                    age = input("Enter new Doctor Age: ")
                    mobile = input("Enter new Doctor Mobile number: ")
                    department = input("Enter new Doctor work department: ")
                    salary = input("Enter new Doctor salary: ")
                    # Write the new details to the file
                    file.write(f"{id}\t\t{name}\t\t{age}\t\t{mobile}\t\t{department}\t\t{salary}\n")
                else:
                    file.write(line)
            if not found:
                print('Doctor not found!')
            else:
                print('Doctor updated successfully.')
                readD()
        c = input('Do you want to update more Doctor records (y/n)? ')

# Function to delete a doctor record by ID
def deleteD():
    id = input('Enter Doctor ID to delete: ')
    with open('DoctorPy.txt', 'r') as file:
        lines = file.readlines()

    with open('DoctorPy.txt', 'w') as file:
        found = False
        for line in lines:
            fields = line.split('\t\t')
            if fields[0] == id:
                found = True
            else:
                file.write(line)
        if not found:
            print('Doctor not found!')
        else:
            print('Doctor deleted successfully.')
            readD()

# Function to display the Doctor Management menu
def homeD():
    while True:
        print('-------------------------')
        print('1: Add New Record')
        print('2: Read All Records')
        print('3: Search For Record')
        print('4: Update Record')
        print('5: Delete Record')
        print('6: Go to Main menu')
        print('7: Exit')
        print('-------------------------\n')
        operation = input('Choose Operation: ')
        if operation == '1':
            writeD()
        elif operation == '2':
            readD()
        elif operation == '3':
            print('1- Search By Id')
            print('2- Search By Name')
            option = input('Choose Option: ')
            if option == '1':
                searchByIdD()
            elif option == '2':
                searchByNameD()
        elif operation == '4':
            updateByIdD()
        elif operation == '5':
            deleteD()
        elif operation == '6':
            main()
        elif operation == '7':
            print('Thank You!')
            break
        else:
            print("Invalid choice!")
        if input('Do you want to perform more operations (y/n)? ').lower() != 'y':
            break

# Function to display the main menu
def main():
    while True:
        print('+----------------------------+')
        print('+ HOSPITAL MANAGEMENT SYSTEM +')
        print('+----------------------------+')
        print('1: Doctor Department')
        print('2: Exit')
        print('---------------------------\n')
        operation = input('Choose Operation: ')
        if operation == '1':
            homeD()
        elif operation == '2':
            print('Thank You!')
            break
        else:
            print("Invalid choice!")
        if input('Do you want to go back to the main menu (y/n)? ').lower() != 'y':
            break

# Run the main function
main()

