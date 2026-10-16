"""
Polymorphism - Program 8:
Create a base class Report with a method generate().
Derive PDFReport, ExcelReport, and HTMLReport.
Override generate() in each class.
Write a function that accepts any report object and calls generate().
"""

class Report:
    def __init__(self, title, data):
        self.title = title
        self.data = data

    def generate(self):
        print(f"Generating generic report for: {self.title}")


class PDFReport(Report):
    def generate(self):
        print(f"[PDF Report Engine] Compiling '{self.title}.pdf'...")
        print("  Formatting vectorized headers, page numbers, and embedded fonts.")
        print(f"  Exporting {len(self.data)} records to PDF successfully.")


class ExcelReport(Report):
    def generate(self):
        print(f"[Excel Report Engine] Generating spreadsheet workbook '{self.title}.xlsx'...")
        print("  Applying cell styling, pivot summaries, and numerical formulas.")
        print(f"  Populated {len(self.data)} rows into active Sheet1.")


class HTMLReport(Report):
    def generate(self):
        print(f"[HTML Report Engine] Building responsive webpage '{self.title}.html'...")
        print("  Rendering Bootstrap responsive tables, CSS stylesheets, and charts.")
        print(f"  Injected {len(self.data)} dynamic JSON data points.")


def process_report(report_object):
    """
    Polymorphic caller function:
    Accepts any object conforming to the Report interface and executes generate().
    """
    print(f"--- Processing Report: {report_object.title} ---")
    report_object.generate()
    print("-" * 55)


if __name__ == "__main__":
    quarterly_data = [{"sales": 15000}, {"sales": 22000}, {"sales": 31000}]

    reports = [
        PDFReport("Q3_Financial_Summary", quarterly_data),
        ExcelReport("Q3_Inventory_Spreadsheet", quarterly_data),
        HTMLReport("Q3_Executive_Dashboard", quarterly_data)
    ]

    print("=== Automated Report Processing Pipeline ===")
    for r in reports:
        process_report(r)
