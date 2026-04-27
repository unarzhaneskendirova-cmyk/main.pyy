import os
print("Checking file...")
if os.path.exists("students.csv"):
    print("File found:students.csv")
else:
    print("Error:students.csv not found.Please download it from LMS")
    exit()


print("Checking output folder...")
if os.path.exists("output"):
    print("Output folder already exists")
else:
    os.makedirs("output")
    print("Output folder created:output/")

#2
import csv
students = []
with open("students.csv",encoding="utf-8") as f:
          reader = csv.DictReader(f)
          for row in reader:
              students.append(row)
                    
print(f"Total students:{len(students)}")
print("First 5 rows:")
print("-----------------------------")
for s in students [:5]:
           print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} GPA:{s['GPA']}")
print("-----------------------------")         
#3
gpas = []
count_high = 0
for s in students:
    gpa = float(s['GPA'])
    gpas.append(gpa)
    if gpa > 3.5:
        count_high += 1
avg_gpa = sum(gpas) / len(gpas)
max_gpa = max(gpas)
min_gpa = min(gpas)
avg_gpa = round(avg_gpa, 2)
print("-----------------------------")
print("GPA Analysis")
print("-----------------------------")
print(f"Total students : {len(students)}")
print(f"Average GPA : {avg_gpa}")
print(f"Highest GPA : {max_gpa}")
print(f"Lowest GPA : {min_gpa}")
print(f"Students GPA>3.5 : {count_high}")
print("-----------------------------")
import json
result = {
    "analysis": "GPA Statistics",
    "total_students": len(students),
    "average_gpa": avg_gpa,
    "max_gpa": max_gpa,
    "min_gpa": min_gpa,
    "high_performers": count_high
}
with open("output/result.json", "w") as f:
    json.dump(result, f, indent=4)
print("\n==============================")
print("ANALYSIS RESULT")
print("==============================")
print("Analysis : GPA Statistics")
print(f"Total students : {len(students)}")
print(f"Average GPA : {avg_gpa}")
print(f"Highest GPA : {max_gpa}")
print(f"Lowest GPA : {min_gpa}")
print(f"High performers : {count_high}")
print("==============================")
print("\nResult saved to output/result.json")
