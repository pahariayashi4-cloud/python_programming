# Hospital Management System: Patient Registration (Dictionary), Appointment Scheduling (List), Medical Records Storage (File Handling), Doctor Information (Tuple), Billing System (Class and Object), Report Generation (Python Libraries) 

#dictionary

# Hospital Management System: Patient Registration (Dictionary), Appointment Scheduling (List), Medical Records Storage (File Handling), Doctor Information (Tuple), Billing System (Class and Object), Report Generation (Python Libraries)

# dictionary

patients = {}

def patient_register():
    p_id = input("enter patient ID: ")
    name = input("enter patient name: ")
    age = input("enter patient age: ")
    disease = input("enter Disease: ")
    contact = input("enter phone no: ")

    patients[p_id] = {
        "name": name,
        "age": age,
        "disease": disease,
        "phone": contact
    }

    print("registered successfully")


# list

appointments = []

def schedule_appointment():
    p_id = input("enter patient ID: ")
    doctor = input("enter doctor name: ")
    date = input("enter appointment date: ")

    appointment = [p_id, doctor, date]
    appointments.append(appointment)

    print("appointment successful")


# tuple

doctors = (
    ("D1", "Dr. Sharma", "Cardiologist"),
    ("D2", "Dr. Roy", "Neurologist"),
    ("D3", "Dr. Sen", "General Physician")
)

def show_doctors():
    print("\nDoctor details")

    for doctor in doctors:
        print("Doctor ID:", doctor[0])
        print("Name:", doctor[1])
        print("specialization:", doctor[2])
        print()


# file handling

def save_record():

    patient_id = input("Enter Patient ID: ")
    record = input("Enter Medical Record: ")

    file = open("medical_records.txt", "a")  # a -> append

    file.write(patient_id + " : " + record + "\n")

    file.close()

    print("Record saved!")


def view_records():

    file = open("medical_records.txt", "r")  # r -> read

    data = file.read()

    print("----- Medical Records -----")
    print(data)

    file.close()


# bill

class Bill:

    def __init__(self, p_name, consultation, medicine, room):
        self.p_name = p_name
        self.consultation = consultation
        self.medicine = medicine
        self.room = room

    def calc_bill(self):
        total = self.consultation + self.medicine + self.room
        return total

    def show_bill(self):
        print("\nBILL")
        print("Patient Name:", self.p_name)
        print("Consultation:", self.consultation)
        print("Medicine:", self.medicine)
        print("Room Charges:", self.room)
        print("Total Bill:", self.calc_bill())


def create_bill():

    name = input("Patient Name: ")

    consultation = float(input("Consultation Charges: "))
    medicine = float(input("Medicine Charges: "))
    room = float(input("Room Charges: "))

    bill = Bill(name, consultation, medicine, room)

    bill.show_bill()


# Main

while True:

    print("1. Patient Registration")
    print("2. Schedule Appointment")
    print("3. Show Doctors")
    print("4. Save Medical Record")
    print("5. View Medical Records")
    print("6. Generate Bill")
    print("7. Generate Patient Report")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        patient_register()

    elif choice == "2":
        schedule_appointment()

    elif choice == "3":
        show_doctors()

    elif choice == "4":
        save_record()

    elif choice == "5":
        view_records()

    elif choice == "6":
        create_bill()

    elif choice == "7":
        print("Report generation coming soon!")

    elif choice == "8":
        print("Thank you")
        break

    else:
        print("Invalid choice. Please try again.")