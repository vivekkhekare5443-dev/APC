"""
Abstraction - Program 5:
Create an abstract class Patient with abstract methods calculate_bill() and treatment().
Derive InPatient, OutPatient, and EmergencyPatient classes and implement the methods
according to the patient type.
"""

from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age

    @abstractmethod
    def treatment(self):
        """Describes treatment regimen."""
        pass

    @abstractmethod
    def calculate_bill(self):
        """Calculates final hospital invoice."""
        pass

    def display_patient_summary(self):
        print(f"[{self.__class__.__name__}] ID: {self.patient_id} | Name: {self.name} (Age: {self.age})")
        print(f"  Regimen: {self.treatment()}")
        print(f"  Total Hospital Bill: Rs. {self.calculate_bill():,.2f}")


class InPatient(Patient):
    def __init__(self, patient_id, name, age, days_admitted, room_rate_per_day=3500, medical_cost=15000):
        super().__init__(patient_id, name, age)
        self.days_admitted = days_admitted
        self.room_rate_per_day = room_rate_per_day
        self.medical_cost = medical_cost

    def treatment(self):
        return f"Admitted in Ward for {self.days_admitted} days with continuous IV fluids, monitoring, and nursing care."

    def calculate_bill(self):
        doctor_visit_fee = self.days_admitted * 1000
        return (self.days_admitted * self.room_rate_per_day) + self.medical_cost + doctor_visit_fee


class OutPatient(Patient):
    def __init__(self, patient_id, name, age, consultation_fee=800, diagnostic_lab_fees=1200):
        super().__init__(patient_id, name, age)
        self.consultation_fee = consultation_fee
        self.diagnostic_lab_fees = diagnostic_lab_fees

    def treatment(self):
        return "Specialist OPD consultation completed; prescription issued for outpatient pharmacy medication."

    def calculate_bill(self):
        return self.consultation_fee + self.diagnostic_lab_fees


class EmergencyPatient(Patient):
    def __init__(self, patient_id, name, age, icu_hours=12, emergency_surgery_cost=45000):
        super().__init__(patient_id, name, age)
        self.icu_hours = icu_hours
        self.emergency_surgery_cost = emergency_surgery_cost

    def treatment(self):
        return f"Immediate trauma resuscitation in Red Zone, emergency surgical stabilization, and {self.icu_hours}h ICU care."

    def calculate_bill(self):
        emergency_triage_fee = 5000
        icu_charge = self.icu_hours * 1500
        return emergency_triage_fee + self.emergency_surgery_cost + icu_charge


if __name__ == "__main__":
    hospital_cases = [
        InPatient("P-IN-101", "Ramesh Gupta", 65, days_admitted=5),
        OutPatient("P-OPD-202", "Diya Patel", 24),
        EmergencyPatient("P-EMG-999", "Arjun Kapoor", 38, icu_hours=8, emergency_surgery_cost=55000)
    ]

    print("=== Hospital Clinical & Billing Management System (Abstraction) ===")
    for case in hospital_cases:
        case.display_patient_summary()
        print("-" * 65)
