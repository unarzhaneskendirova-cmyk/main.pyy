import os
import csv
import json


# ---------- FileManager ----------
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")

        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found.")
            return False

    def create_output_folder(self):
        print("\nChecking output folder...")

        if os.path.exists("output"):
            print("Output folder already exists: output/")
        else:
            os.makedirs("output")
            print("Output folder created: output/")


# ---------- DataLoader ----------
class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("\nLoading data...")

        try:
            with open(self.filename, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.students.append(row)

            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return []

    def preview(self, n=5):
        print("\nFirst rows:")
        print("-----------------------------")

        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")

        print("-----------------------------")


# ---------- DataAnalyser ----------
class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        gpas = []
        count_high = 0

        for s in self.students:
            try:
                gpa = float(s['GPA'])
            except ValueError:
                continue

            gpas.append(gpa)

            if gpa > 3.5:
                count_high += 1

        avg_gpa = round(sum(gpas) / len(gpas), 2)
        max_gpa = max(gpas)
        min_gpa = min(gpas)

        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(self.students),
            "average_gpa": avg_gpa,
            "max_gpa": max_gpa,
            "min_gpa": min_gpa,
            "high_performers": count_high
        }

        return self.result

    def print_results(self):
        print("\n-----------------------------")
        print("GPA Analysis")
        print("-----------------------------")

        print(f"Total students : {self.result['total_students']}")
        print(f"Average GPA : {self.result['average_gpa']}")
        print(f"Highest GPA : {self.result['max_gpa']}")
        print(f"Lowest GPA : {self.result['min_gpa']}")
        print(f"Students GPA>3.5 : {self.result['high_performers']}")

        print("-----------------------------")


# ---------- ResultSaver ----------
class ResultSaver:
    def __init__(self, result):
        self.result = result

    def save_json(self):
        try:
            with open("output/result.json", "w") as f:
                json.dump(self.result, f, indent=4)

            print("\nResult saved to output/result.json")

        except Exception:
            print("Error saving file.")


# ---------- MAIN ----------
fm = FileManager("students.csv")

if not fm.check_file():
    print("Stopping program.")
else:
    fm.create_output_folder()

    dl = DataLoader("students.csv")
    students = dl.load()

    if students:
        dl.preview()

        analyser = DataAnalyser(students)
        result = analyser.analyse()
        analyser.print_results()

        saver = ResultSaver(result)
        saver.save_json()
