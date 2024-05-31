import os

# Function to add a new patient record
def writeP():
    id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Patient Age: ")
    mobile = input("Enter Patient Mobile: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    with open('PatientPy.txt', 'a') as file:
        file.write(f"{id}\t\t{name}\t\t{age}\t\t{mobile}\t\t{department}\t\t{salary}\n")

    print('Patient record added successfully.')

# Function to read and display all patient records
def readP():
    with open('PatientPy.txt', 'r') as file:
        print(file.read())

# Function to search for a patient by ID
def searchByIdP():
    id = input("Enter Patient ID: ")
    with open('PatientPy.txt', 'r') as file:
        found = False
        for line in file:
            fields = line.split('\t\t')
            if fields[0] == id:
                print(line)
                found = True
                break
        if not found:
            print("Patient not found!")

# Function to delete a patient record by ID
def deleteP():
    id = input("Enter Patient ID to delete: ")
    with open('PatientPy.txt', 'r') as file:
        lines = file.readlines()

    with open('PatientPy.txt', 'w') as file:
        found = False
        for line in lines:
            fields = line.split('\t\t')
            if fields[0] == id:
                found = True
            else:
                file.write(line)

        if found:
            print('Patient record deleted successfully.')
        else:
            print('Patient not found!')

# Function to display the Patient Management menu
def homeP():
    while True:
        print("\nPatient Management Menu:")
        print("1. Add Patient Record")
        print("2. Read All Patient Records")
        print("3. Search Patient by ID")
        print("4. Delete Patient by ID")
        print("5. Go Back to Main Menu")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            writeP()
        elif choice == '2':
            readP()
        elif choice == '3':
            searchByIdP()
        elif choice == '4':
            deleteP()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Function to add a new doctor record
def writeD():
    id = input("Enter Doctor ID: ")
    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")

    with open('DoctorPy.txt', 'a') as file:
        file.write(f"{id}\t\t{name}\t\t{specialization}\n")

    print('Doctor record added successfully.')

# Function to read and display all doctor records
def readD():
    with open('DoctorPy.txt', 'r') as file:
        print(file.read())

# Function to search for a doctor by ID
def searchByIdD():
    id = input("Enter Doctor ID: ")
    with open('DoctorPy.txt', 'r') as file:
        found = False
        for line in file:
            fields = line.split('\t\t')
            if fields[0] == id:
                print(line)
                found = True
                break
        if not found:
            print("Doctor not found!")

# Function to delete a doctor record by ID
def deleteD():
    id = input("Enter Doctor ID to delete: ")
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

        if found:
            print('Doctor record deleted successfully.')
        else:
            print('Doctor not found!')

# Function to display the Doctor Management menu
def homeD():
    while True:
        print("\nDoctor Management Menu:")
        print("1. Add Doctor Record")
        print("2. Read All Doctor Records")
        print("3. Search Doctor by ID")
        print("4. Delete Doctor by ID")
        print("5. Go Back to Main Menu")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            writeD()
        elif choice == '2':
            readD()
        elif choice == '3':
            searchByIdD()
        elif choice == '4':
            deleteD()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Function to display the main menu
def main():
    while True:
        print("\nMain Menu:")
        print("1. Patient Department")
        print("2. Doctor Department")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            homeP()
        elif choice == '2':
            homeD()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
main()
