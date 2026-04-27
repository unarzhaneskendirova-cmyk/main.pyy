import os
import csv
def check_files():
    print("Checking file...")
    if os.path.exists("students.csv"):
        print("File found: students.csv")
    else:
        print("Error: students.csv not found.")
        return False
    print("\nChecking output folder...")
    if os.path.exists("output"):
        print("Output folder already exists: output/")
    else:
        os.makedirs("output")
        print("Output folder created: output/")
    return True
def load_data(filename):
    print("\nLoading data...")
    students = []
    try:
        with open(filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(row)
        print(f"Data loaded successfully: {len(students)} students")
        return students
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception:
        print("Error while loading data.")
        return []
def preview_data(students, n=5):
    print("\nFirst rows:")
    print("-----------------------------")
    for s in students[:n]:
        print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
    print("-----------------------------")
def analyse_gpa(students):
    gpas = []
    count_high = 0
    for s in students:
        try:
            gpa = float(s['GPA'])
        except ValueError:
            print(f"Warning: invalid GPA for {s['student_id']}")
            continue
        gpas.append(gpa)
        if gpa > 3.5:
         count_high += 1
    avg_gpa = round(sum(gpas) / len(gpas), 2)
    max_gpa = max(gpas)
    min_gpa = min(gpas)
    return {
        "analysis": "GPA Statistics",
        "total_students": len(students),
        "average_gpa": avg_gpa,
        "max_gpa": max_gpa,
        "min_gpa": min_gpa,
        "high_performers": count_high
    }
def lambda_tasks(students):
    print("\n-----------------------------")
    print("Lambda / Map / Filter")
    print("-----------------------------")
    high_gpa = list(filter(lambda s: float(s['GPA']) > 3.8, students))
    print(f"GPA > 3.8 : {len(high_gpa)}")
    gpa_values = list(map(lambda s: float(s['GPA']), students))
    print(f"GPA values (first 5) : {gpa_values[:5]}")
    hard_workers = list(filter(lambda s: float(s['study_hours_per_day']) > 4, students))
    print(f"study_hours_per_day > 4 : {len(hard_workers)}")
    print("-----------------------------")
import json
def save_to_json(result):
    with open("output/result.json", "w") as f:
        json.dump(result, f, indent=4)
def print_analysis(result):
    print("\n==============================")
    print("ANALYSIS RESULT")
    print("==============================")
    print("Analysis : GPA Statistics")
    print(f"Total students : {result['total_students']}")
    print(f"Average GPA : {result['average_gpa']}")
    print(f"Highest GPA : {result['max_gpa']}")
    print(f"Lowest GPA : {result['min_gpa']}")
    print(f"High performers : {result['high_performers']}")
    print("==============================")
    print("\nResult saved to output/result.json")
if check_files():
    students = load_data("students.csv")
    if students:
        preview_data(students)
        # GPA Analysis
        result = analyse_gpa(students)
        print("\n-----------------------------")
        print("GPA Analysis")
        print("-----------------------------")
        print(f"Total students : {result['total_students']}")
        print(f"Average GPA : {result['average_gpa']}")
        print(f"Highest GPA : {result['max_gpa']}")
        print(f"Lowest GPA : {result['min_gpa']}")
        print(f"Students GPA>3.5 : {result['high_performers']}")
        print("-----------------------------")
        # Lambda / Map / Filter
        print("\n-----------------------------")
        print("Lambda / Map / Filter")
        print("-----------------------------")
        high_gpa = list(filter(lambda s: float(s['GPA']) > 3.8, students))
        print(f"Students with GPA > 3.8 : {len(high_gpa)}")
        gpa_values = list(map(lambda s: float(s['GPA']), students))
        print(f"GPA values (first 5) : {gpa_values[:5]}")
        hard_workers = list(filter(lambda s: float(s['study_hours_per_day']) > 4, students))
        print(f"Students studying > 4 hours : {len(hard_workers)}")
        print("-----------------------------")
        # JSON сохранение
        save_to_json(result)
        # Проверка ошибки (как в задании)
        print("\nLoading data...")
        load_data("wrong_file.csv")
