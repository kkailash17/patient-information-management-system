import pandas as pd
import matplotlib.pyplot as plt


# ---------------- DATA FUNCTIONS ---------------- #

def load_data():
    try:
        return pd.read_csv('patient_data.csv', index_col='PatientID')
    except FileNotFoundError:
        return pd.DataFrame(columns=['Name', 'Age', 'Gender', 'Contact', 'Reason'])


def save_data(data):
    data.to_csv('patient_data.csv', index=True)


# ---------------- USER FUNCTIONS ---------------- #

def create_account():
    print("\nCreate Account")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("Account created successfully!")


def login():
    print("\nLogin")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("Login successful!")


def about_us():
    print("\nAbout Us")
    print("Patient Information Management System")
    print("A simple system to manage and store patient records.")
    print("Developed by Kailash\n")


# ---------------- GRAPH FUNCTION ---------------- #

def display_histogram(data):
    if data.empty:
        print("No patient data available.")
        return

    ages = data['Age'].astype(int)

    plt.hist(ages, bins=5)
    plt.title('Patient Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Number of Patients')
    plt.show()


# ---------------- MENUS ---------------- #

def main_menu():
    print("\nPatient Information System")
    print("1. About Us")
    print("2. Login")
    print("3. Create Account")
    print("4. Exit")


def patient_menu():
    print("\nPatient Menu")
    print("1. Add Patient")
    print("2. Search Patient")
    print("3. Update Patient")
    print("4. Delete Patient")
    print("5. Display Age Distribution")
    print("6. View All Patients")
    print("7. Logout")


# ---------------- PATIENT FUNCTIONS ---------------- #

def add_patient(data):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    contact = input("Enter patient contact number: ")
    reason = input("Reason for hospital admission: ")

    patient_id = data.index.max() + 1 if not data.empty else 1
    data.loc[patient_id] = [name, age, gender, contact, reason]

    print("Patient record added successfully!")


def search_patient(data):

    print("\nSearch Patient By:")
    print("1. Patient ID")
    print("2. Name")
    print("3. Age")
    print("4. Gender")

    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            patient_id = int(input("Enter Patient ID: "))
            if patient_id in data.index:
                print("\nPatient Information:")
                print(data.loc[patient_id])
            else:
                print("Patient not found.")
        except ValueError:
            print("Invalid ID.")

    elif choice == '2':
        name = input("Enter patient name: ")
        result = data[data['Name'].str.contains(name, case=False)]

        if result.empty:
            print("No patient found.")
        else:
            print(result)

    elif choice == '3':
        try:
            age = int(input("Enter age: "))
            result = data[data['Age'] == age]

            if result.empty:
                print("No patient found.")
            else:
                print(result)
        except ValueError:
            print("Invalid age.")

    elif choice == '4':
        gender = input("Enter gender (Male/Female): ")
        result = data[data['Gender'].str.lower() == gender.lower()]

        if result.empty:
            print("No patient found.")
        else:
            print(result)

    else:
        print("Invalid choice.")


def update_patient(data):
    try:
        patient_id = int(input("Enter patient ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    if patient_id in data.index:
        print("\nCurrent Patient Information:")
        print(data.loc[patient_id])

        name = input("Enter new name (press enter to keep same): ")
        age = input("Enter new age (press enter to keep same): ")
        gender = input("Enter new gender (press enter to keep same): ")
        contact = input("Enter new contact (press enter to keep same): ")
        reason = input("Enter new reason (press enter to keep same): ")

        if name:
            data.loc[patient_id, 'Name'] = name
        if age:
            data.loc[patient_id, 'Age'] = int(age)
        if gender:
            data.loc[patient_id, 'Gender'] = gender
        if contact:
            data.loc[patient_id, 'Contact'] = contact
        if reason:
            data.loc[patient_id, 'Reason'] = reason

        print("Patient record updated successfully!")
    else:
        print("Patient not found.")


def delete_patient(data):
    try:
        patient_id = int(input("Enter patient ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    if patient_id in data.index:
        data.drop(patient_id, inplace=True)
        print("Patient record deleted successfully!")
    else:
        print("Patient not found.")


def view_all_patients(data):
    if data.empty:
        print("No records found.")
    else:
        print("\nAll Patient Records:")
        print(data)


# ---------------- MAIN PROGRAM ---------------- #

if __name__ == "__main__":

    about_us()

    while True:
        main_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            about_us()

        elif choice == '2':
            login()
            patients = load_data()

            while True:
                patient_menu()
                patient_choice = input("Enter your choice (1-7): ")

                if patient_choice == '1':
                    add_patient(patients)

                elif patient_choice == '2':
                    search_patient(patients)

                elif patient_choice == '3':
                    update_patient(patients)

                elif patient_choice == '4':
                    delete_patient(patients)

                elif patient_choice == '5':
                    display_histogram(patients)

                elif patient_choice == '6':
                    view_all_patients(patients)

                elif patient_choice == '7':
                    save_data(patients)
                    print("Logging out. Data saved.")
                    break

                else:
                    print("Invalid choice.")

        elif choice == '3':
            create_account()

        elif choice == '4':
            print("Thank You. Have a Wonderful Day!.")
            break

        else:
            print("Invalid choice.")
