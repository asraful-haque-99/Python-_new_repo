from datetime import datetime

# Patient Registration - Dictionary
patients = {}

# Appointment Scheduling - List
appointments = []

# Doctor Information - Tuple
doctors = (
    ("D001", "Dr. Sharma", "Cardiologist"),
    ("D002", "Dr. Khan", "Neurologist"),
    ("D003", "Dr. Roy", "General Physician")
)

# Billing System - Class and Object
class Billing:
    def __init__(self, patient_id, amount):
        self.patient_id = patient_id
        self.amount = amount

    def show_bill(self):
        print("Patient ID:", self.patient_id)
        print("Bill Amount:", self.amount)


def register_patient():
    pid = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    disease = input("Enter Disease: ")

    patients[pid] = {
        "name": name,
        "age": age,
        "disease": disease
    }

    print("Patient registered successfully!")


def schedule_appointment():
    pid = input("Enter Patient ID: ")
    doctor = input("Enter Doctor Name: ")
    date = input("Enter Appointment Date: ")

    appointment = (pid, doctor, date)
    appointments.append(appointment)

    print("Appointment scheduled successfully!")


def show_doctors():
    print("\nDoctor Information")
    for doctor in doctors:
        print("ID:", doctor[0],
              "Name:", doctor[1],
              "Specialization:", doctor[2])


def medical_record():
    pid = input("Enter Patient ID: ")
    record = input("Enter Medical Record: ")

    with open("medical_records.txt", "a") as file:
        file.write(pid + " : " + record + "\n")

    print("Medical record saved!")


def generate_report():
    print("\n----- HOSPITAL REPORT -----")

    print("\nRegistered Patients:")
    for pid, data in patients.items():
        print(pid, data)

    print("\nAppointments:")
    for appointment in appointments:
        print(appointment)

    print("\nDoctors:")
    show_doctors()

    with open("hospital_report.txt", "w") as file:
        file.write("HOSPITAL MANAGEMENT REPORT\n")
        file.write("Generated: " + str(datetime.now()) + "\n\n")

        file.write("PATIENTS\n")
        for pid, data in patients.items():
            file.write(str(pid) + " " + str(data) + "\n")

        file.write("\nAPPOINTMENTS\n")
        for appointment in appointments:
            file.write(str(appointment) + "\n")

        file.write("\nDOCTORS\n")
        for doctor in doctors:
            file.write(str(doctor) + "\n")

    print("\nReport generated successfully!")


# Main Program
while True:
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Patient Registration")
    print("2. Schedule Appointment")
    print("3. Show Doctor Information")
    print("4. Medical Records")
    print("5. Billing")
    print("6. Generate Report")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        register_patient()

    elif choice == 2:
        schedule_appointment()

    elif choice == 3:
        show_doctors()

    elif choice == 4:
        medical_record()

    elif choice == 5:
        pid = input("Enter Patient ID: ")
        amount = float(input("Enter Bill Amount: "))

        bill = Billing(pid, amount)
        bill.show_bill()

    elif choice == 6:
        generate_report()

    elif choice == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")