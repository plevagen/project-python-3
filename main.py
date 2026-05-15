import os
import csv
import json
from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser, SleepAnalyser

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