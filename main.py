import os
import csv
import json

class FileManager:
    def __init__(self, filename):
        self.filename = filename
    def check_file(self):
        print("Checking File...")

        if os.path.exists(self.filename):
            print("File found: " + self.filename)
            return True
        else:
            print("Error: " + self.filename + "file not found")
            return False
    def create_output_folder(self, folder = 'output'):
        print("Checking output folder...")

        if os.path.exists(folder):
            print("Output folder already exists")
        else:
            os.makedirs(folder)
            print("Output folder created: " + folder)

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []
    def load(self):
        print("Loading data...")

        try:
            with open(self.filename, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.students.append(row)
            print("Data loaded successfully: " + str(len(self.students)) + " students")
        except FileNotFoundError:
            print("Error: file " + self.filename + " not found. Please check the filename")
        except Exception as e:
            print("An unexpected error occured" + str(e)) 

    def preview(self, n = 5):
        print("First 5 rows: ")
        print("-" * 30)

        for i in range(n):
            s = self.students[i]
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
        
        print('-' * 30)

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}
    def analyse(self):
        gpas = []
        high_performers = 0

        for s in self.students:
            try:
                gpa = float(s['GPA'])
                gpas.append(gpa)
                if gpa > 3.5:
                    high_performers += 1
            except ValueError:
                print("Warning: could not convert value for student" + s['student_id'] + "- skipping row")
                continue
        
        avg_gpa = round(sum(gpas) / len(gpas), 2)
        max_gpa = max(gpas)
        min_gpa = min(gpas)

        self.result = {
            "analysis" : "GPA Statistics",
            "total_students" : len(self.students),
            "average_gpa" : avg_gpa,
            "max_gpa": max_gpa,
            "min_gpa": min_gpa,                       
            "high_performers": high_performers
        }
        return self.result
    
    def print_results(self):
        print("-" * 30)
        print("GPA Analysis")
        print("-" * 30)
        print(f"{'Total students':<20} : {self.result['total_students']}")
        print(f"{'Average GPA':<20} : {self.result['average_gpa']}")
        print(f"{'Highest GPA':<20} : {self.result['max_gpa']}")
        print(f"{'Lowest GPA':<20} : {self.result['min_gpa']}")
        print(f"{'Students GPA>3.5':<20} : {self.result['high_performers']}")
        print("-" * 30)


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path
    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent = 4)
            print("Result saved to " + self.output_path)
        except Exception as e:
            print("Error saving file" + str(e))

def lambda_map_filter(students):
    print("-" * 30)
    print("Lambda / Map / Filter")
    print("-" * 30)

    high_gpa = list(filter(lambda s : float(s['GPA']) > 3.8, students))
    print(f"{'GPA > 3.8': <30} : {len(high_gpa)}")

    gpa_values = list(map(lambda s: float(s['GPA']), students))
    print(f"{'GPA values(first 5)' : <30} : {gpa_values[:5]}")

    hard_workers = list(filter(lambda s : float(s['study_hours_per_day']) > 4, students))
    print(f"{'study_hours_per_day > 4': <30} :{len(hard_workers)}")

    print("-" * 30)

def test_exception_handling():
    bad_loader = DataLoader("wrong_file.csv")
    bad_loader.load()

def print_final_summary(result):
    print("=" * 30)
    print("ANALYSIS RESULT")
    print("=" * 30)
    print(f"{'Analysis':<20} : {result['analysis']}")
    print(f"{'Total students':<20} : {result['total_students']}")
    print(f"{'Average GPA':<20} : {result['average_gpa']}")
    print(f"{'Highest GPA':<20} : {result['max_gpa']}")
    print(f"{'Lowest GPA':<20} : {result['min_gpa']}")
    print(f"{'High performers':<20} : {result['high_performers']}")
    print("=" * 30)

if __name__ == "__main__":
    fm = FileManager('students.csv')

    if not fm.check_file():
        print("Stopping program")
        exit()
    fm.create_output_folder()

    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()
    print_final_summary(analyser.result)

    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()

    lambda_map_filter(dl.students)
    test_exception_handling()