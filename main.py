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
            print("Data loaded succesfully: " + str(len(self.students)) + "students")
        except FileNotFoundError:
            print("Error: file" + self.filename + "not found. Please check the filename")
        except Exception as e:
            print("An unexpected error occured" + str(e)) 

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}
    def analyse(self):
        gpas = []
        high_performers = 0

        for s in self.students:
            try:
                gpa = float(s(['GPA']))
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
            "Analysis" : "GPA Statistics",
            "total_students" : len(self.students),
            "average gpa" : avg_gpa,
            "max_gpa": max_gpa,
            "min_gpa": min_gpa,                       
            "high_performers": high_performers
        }
        return self.result
    
    def print_results(self):
        print("-" * 30)
        print("GPA Analysis")
        print("-" * 30)
        print("Total Students: " + self.result['total_students'])
        print("Average GPA: " + self.result['avg_gpa'])
        print("Highest GPA: " + self.result['max_gpa'])
        print("Lowest GPA: " + self.result['min_gpa'])
        print("Students GPA > 3.5: " + self.result['high_performers'])
        print("-" * 30)

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.result = output_path
    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent = 4)
            print("Result saved to" + self.output_path)
        except Exception as e:
            print("Error saving file" + str(e))
