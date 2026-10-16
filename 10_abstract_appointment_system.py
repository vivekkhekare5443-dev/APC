"""
Abstraction - Program 10:
Create an abstract class Appointment with abstract methods book_appointment() and calculate_fee().
Derive GeneralAppointment, SpecialistAppointment, and EmergencyAppointment.
"""

from abc import ABC, abstractmethod

class Appointment(ABC):
    def __init__(self, patient_name, doctor_name, preferred_date):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.preferred_date = preferred_date
        self.is_confirmed = False

    @abstractmethod
    def book_appointment(self):
        """Schedules and books the consultation slot."""
        pass

    @abstractmethod
    def calculate_fee(self):
        """Calculates total consultation fee."""
        pass

    def display_appointment_details(self):
        print(f"[{self.__class__.__name__}]")
        print(f"  Patient : {self.patient_name} | Doctor: {self.doctor_name}")
        print(f"  Date    : {self.preferred_date} | Status: {'CONFIRMED' if self.is_confirmed else 'PENDING'}")
        print(f"  Fee     : Rs. {self.calculate_fee():,.2f}")


class GeneralAppointment(Appointment):
    def __init__(self, patient_name, doctor_name, preferred_date, consultation_fee=500):
        super().__init__(patient_name, doctor_name, preferred_date)
        self.consultation_fee = consultation_fee

    def book_appointment(self):
        self.is_confirmed = True
        print(f"[General OPD] Appointment booked with {self.doctor_name} for regular health checkup on {self.preferred_date}.")

    def calculate_fee(self):
        return float(self.consultation_fee)


class SpecialistAppointment(Appointment):
    def __init__(self, patient_name, doctor_name, preferred_date, specialization, base_fee=1200, procedure_fee=800):
        super().__init__(patient_name, doctor_name, preferred_date)
        self.specialization = specialization
        self.base_fee = base_fee
        self.procedure_fee = procedure_fee

    def book_appointment(self):
        self.is_confirmed = True
        print(f"[Specialist Clinic] Slot reserved with {self.specialization} specialist {self.doctor_name} on {self.preferred_date}.")

    def calculate_fee(self):
        return float(self.base_fee + self.procedure_fee)


class EmergencyAppointment(Appointment):
    def __init__(self, patient_name, doctor_name, emergency_level="Priority 1"):
        # Emergency appointment is immediate (no prior preferred date required)
        super().__init__(patient_name, doctor_name, preferred_date="IMMEDIATE / NOW")
        self.emergency_level = emergency_level

    def book_appointment(self):
        self.is_confirmed = True
        print(f"[EMERGENCY TRAUMA] IMMEDIATE code activated for patient {self.patient_name}! Assigned to {self.doctor_name} ({self.emergency_level}).")

    def calculate_fee(self):
        emergency_admission_surcharge = 2500
        specialist_on_call_fee = 2000
        return float(emergency_admission_surcharge + specialist_on_call_fee)


if __name__ == "__main__":
    appointments = [
        GeneralAppointment("Aarav Sharma", "Dr. K. L. Rao", "2026-11-05"),
        SpecialistAppointment("Diya Patel", "Dr. Priya Nair", "2026-11-06", specialization="Cardiology"),
        EmergencyAppointment("Rohan Verma", "Dr. Mehta (Trauma Lead)", emergency_level="Critical")
    ]

    print("=== Hospital Appointment Scheduling Hub (Abstraction Interface) ===")
    for appt in appointments:
        print()
        appt.book_appointment()
        appt.display_appointment_details()
