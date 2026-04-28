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