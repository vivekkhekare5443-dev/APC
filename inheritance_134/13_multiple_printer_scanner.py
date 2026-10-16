"""
Inheritance - Program 13 (Multiple Inheritance):
Create classes Printer and Scanner with suitable methods for printing and scanning documents.
Create a MultifunctionDevice class that inherits from both and supports both operations.
"""

class Printer:
    def __init__(self, print_speed_ppm):
        self.print_speed_ppm = print_speed_ppm

    def print_document(self, document_name):
        print(f"[Printer] Printing document '{document_name}' at {self.print_speed_ppm} pages per minute...")


class Scanner:
    def __init__(self, scan_resolution_dpi):
        self.scan_resolution_dpi = scan_resolution_dpi

    def scan_document(self, document_name):
        print(f"[Scanner] Scanning document '{document_name}' at {self.scan_resolution_dpi} DPI optical resolution...")


class MultifunctionDevice(Printer, Scanner):
    def __init__(self, device_model, print_speed_ppm, scan_resolution_dpi):
        Printer.__init__(self, print_speed_ppm)
        Scanner.__init__(self, scan_resolution_dpi)
        self.device_model = device_model

    def display_specs(self):
        print(f"=== Multi-Function Device: {self.device_model} ===")
        print(f"Printing Speed     : {self.print_speed_ppm} PPM")
        print(f"Optical Resolution : {self.scan_resolution_dpi} DPI")

    def photocopy(self, document_name):
        print(f"[MFD] Executing 2-in-1 Photocopy of '{document_name}':")
        self.scan_document(document_name)
        self.print_document(f"{document_name} (Copy)")


if __name__ == "__main__":
    mfd = MultifunctionDevice("HP LaserJet Pro MFP 4104", print_speed_ppm=40, scan_resolution_dpi=1200)
    mfd.display_specs()
    print()
    mfd.print_document("Semester_Project_Report.pdf")
    mfd.scan_document("Signed_Admission_Form.pdf")
    print()
    mfd.photocopy("ID_Card.png")
