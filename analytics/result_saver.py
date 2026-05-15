import json

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