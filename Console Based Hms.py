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
        data = file.read()
    print(data)

# Function to search for a patient by ID
def searchByIdP():
    id = input("Enter Patient ID: ")
    with open('PatientPy.txt', 'r') as file:
        found = False
        for line in file:
            fields = line.split('\t\t')
            if fields[0] == id:
                print(f"ID\t\tName\t\tAge\t\tMobile\t\tDepartment\t\tSalary\n{'-' * 95}\n{line}")
                found = True
                break
        if not found:
            print("Patient not found!")

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
        data = file.read()
    print(data)

# Function to search for a doctor by ID
def searchByIdD():
    id = input("Enter Doctor ID: ")
    with open('DoctorPy.txt', 'r') as file:
        found = False
        for line in file:
            fields = line.split('\t\t')
            if fields[0] == id:
                print(f"ID\t\tName\t\tSpecialization\n{'-' * 50}\n{line}")
                found = True
                break
        if not found:
            print("Doctor not found!")

# Function to display the main menu
def main():
    while True:
        print("\n--- Hospital Management System Menu ---")
        print("1. Patient Department")
        print("2. Doctor Department")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            patient_department()
        elif choice == "2":
            doctor_department()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Function to handle patient department operations
def patient_department():
    while True:
        print("\n--- Patient Department Menu ---")
        print("1. Add Patient Record")
        print("2. Read All Patient Records")
        print("3. Search Patient by ID")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            writeP()
        elif choice == "2":
            readP()
        elif choice == "3":
            searchByIdP()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Function to handle doctor department operations
def doctor_department():
    while True:
        print("\n--- Doctor Department Menu ---")
        print("1. Add Doctor Record")
        print("2. Read All Doctor Records")
        print("3. Search Doctor by ID")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            writeD()
        elif choice == "2":
            readD()
        elif choice == "3":
            searchByIdD()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the main function
main()


