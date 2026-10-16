"""
Inheritance - Program 18 (Hybrid: Hierarchical + Multiple Inheritance):
Create a class Person and derive Doctor and Patient.
Create additional classes representing Surgeon and MedicalResearcher.
Design the hierarchy so that the program demonstrates multiple inheritance
along with hierarchical inheritance.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age} years")


# Hierarchical Inheritance 1: Doctor from Person
class Doctor(Person):
    def __init__(self, name, age, license_no, specialization):
        super().__init__(name, age)
        self.license_no = license_no
        self.specialization = specialization

    def display_doctor(self):
        self.display_person()
        print(f"License No     : {self.license_no}")
        print(f"Specialization : {self.specialization}")


# Hierarchical Inheritance 2: Patient from Person
class Patient(Person):
    def __init__(self, name, age, patient_id, ailment):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.ailment = ailment

    def display_patient(self):
        print("--- Patient Record ---")
        self.display_person()
        print(f"Patient ID : {self.patient_id}")
        print(f"Ailment    : {self.ailment}")


# Multilevel Inheritance: Surgeon from Doctor
class Surgeon(Doctor):
    def __init__(self, name, age, license_no, specialization, surgeries_performed):
        super().__init__(name, age, license_no, specialization)
        self.surgeries_performed = surgeries_performed

    def display_surgeon(self):
        self.display_doctor()
        print(f"Surgeries Completed : {self.surgeries_performed}")


# Independent Researcher Class
class MedicalResearcher:
    def __init__(self, lab_affiliation, grant_funding):
        self.lab_affiliation = lab_affiliation
        self.grant_funding = grant_funding

    def display_researcher(self):
        print(f"Laboratory    : {self.lab_affiliation}")
        print(f"Grant Funding : Rs. {self.grant_funding:,.2f}")


# Multiple Inheritance: AcademicSurgeon combines Surgeon and MedicalResearcher
class AcademicSurgeon(Surgeon, MedicalResearcher):
    def __init__(self, name, age, license_no, specialization, surgeries_performed, lab_affiliation, grant_funding, ongoing_clinical_trials):
        Surgeon.__init__(self, name, age, license_no, specialization, surgeries_performed)
        MedicalResearcher.__init__(self, lab_affiliation, grant_funding)
        self.ongoing_clinical_trials = ongoing_clinical_trials

    def display_profile(self):
        print("=== Academic Surgeon Profile (Hybrid: Hierarchical + Multiple) ===")
        self.display_surgeon()
        self.display_researcher()
        print(f"Clinical Trials : {self.ongoing_clinical_trials} active projects")


if __name__ == "__main__":
    p = Patient("Ramesh Gupta", 58, "PT-104", "Coronary Artery Blockage")
    p.display_patient()
    print()

    lead_doc = AcademicSurgeon(
        name="Dr. Shashi Sen",
        age=48,
        license_no="MCI-SURG-7821",
        specialization="Cardiothoracic Surgery",
        surgeries_performed=450,
        lab_affiliation="National Institute of Cardiovascular Research",
        grant_funding=2500000.0,
        ongoing_clinical_trials=3
    )
    lead_doc.display_profile()
