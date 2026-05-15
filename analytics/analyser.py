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