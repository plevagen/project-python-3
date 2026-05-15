import os

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