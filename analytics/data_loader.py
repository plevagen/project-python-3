import csv

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