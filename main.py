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
        print("=" * 30)

        for i in range(n):
            s = self.students[i]
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
        
        print('=' * 30)

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}
    
    def analyse(self):
        print("Not implemented - use a child class")
    
    def print_results(self):
        print("=" * 30)
        print(self.result.get("analysis", "Results"))
        print("=" * 30)
        for key, values in self.result.items():
            if key != "analysis":
                print(f"{key:<20} : {values}")
        print("=" * 30)
    
    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)
    
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
            "analysis" : "GPA analysis",
            "total_students" : len(self.students),
            "average_gpa" : avg_gpa,
            "max_gpa": max_gpa,
            "min_gpa": min_gpa,                       
            "high_performers": high_performers
        }
    
    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"
    
    def print_results(self):
        print("=" * 30)
        print("GPA ANALYSIS RESULTS")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

class SleepAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)
    
    def analyse(self):
        low_sleep = []
        high_sleep = []

        for s in self.students:
            try:
                sleep = float(s['sleep_hours'])
                gpa = float(s['GPA'])

                if sleep < 6:
                    low_sleep.append(gpa)
                else:
                    high_sleep.append(gpa)
            except ValueError:
                print(f"Warning: could not convert value for student {s['student_id']} - skipping row")
                continue
        
        avg_gpa_low = round(sum(low_sleep) / len(low_sleep), 2) if low_sleep else 0
        avg_gpa_high = round(sum(high_sleep) / len(high_sleep), 2) if high_sleep else 0
        gpa_diff = round(avg_gpa_high - avg_gpa_low, 2)
    
        self.result = {
            "analysis":       "Sleep vs GPA",
            "total_students": len(self.students),
            "low_sleep_students":  len(low_sleep),
            "low_sleep_avg_gpa":   avg_gpa_low,
            "high_sleep_students": len(high_sleep),
            "high_sleep_avg_gpa":  avg_gpa_high,
            "gpa_difference":      gpa_diff
        }

    def print_results(self):
        r = self.result
        print("=" * 30)
        print("SLEEP ANALYSIS RESULT")
        print("=" * 30)
        print(f"{'Analysis':<20} : {r['analysis']}")
        print(f"{'Total students':<20} : {r['total_students']}")
        print("-" * 30)
        print("Sleep < 6 hours:")
        print(f"  {'Students':<18} : {r['low_sleep_students']}")
        print(f"  {'Average GPA':<18} : {r['low_sleep_avg_gpa']}")
        print("Sleep >= 6 hours:")
        print(f"  {'Students':<18} : {r['high_sleep_students']}")
        print(f"  {'Average GPA':<18} : {r['high_sleep_avg_gpa']}")
        print("-" * 30)
        print(f"{'GPA difference':<20} : {r['gpa_difference']}")
        print("=" * 30)

    def __str__(self):
        return f"SleepAnalyser: Sleep vs GPA, {len(self.students)} students"

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

class Report:
    def __init__(self, analyser, saver):
        self.analyser = analyser
        self.saver = saver
    def generate(self):
        print("Generating report...")
        self.analyser.analyse()
        self.analyser.print_results()
        self.saver.save_json()
        print("Report Complete")

def lambda_map_filter(students):
    print("=" * 30)
    print("Lambda / Map / Filter")
    print("=" * 30)

    high_gpa = list(filter(lambda s : float(s['GPA']) > 3.8, students))
    print(f"{'GPA > 3.8': <30} : {len(high_gpa)}")

    gpa_values = list(map(lambda s: float(s['GPA']), students))
    print(f"{'GPA values(first 5)' : <30} : {gpa_values[:5]}")

    hard_workers = list(filter(lambda s : float(s['study_hours_per_day']) > 4, students))
    print(f"{'study_hours_per_day > 4': <30} :{len(hard_workers)}")

    print("=" * 30)

def test_exception_handling():
    bad_loader = DataLoader("wrong_file.csv")
    bad_loader.load()

if __name__ == "__main__":
    fm = FileManager('students.csv')

    if not fm.check_file():
        print("Stopping program")
        exit()
    fm.create_output_folder()

    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    analysers = [GpaAnalyser(dl.students), SleepAnalyser(dl.students)]
    print("=" * 30)
    print("Running all analysers: ")
    print("=" * 30)
    for a in analysers:
        print(a)
        a.analyse()
        a.print_results()
    
    saver = ResultSaver(analysers[0].result, 'output/result.json')
    report = Report(analysers[0], saver)
    report.generate()
    
    lambda_map_filter(dl.students)
    test_exception_handling()