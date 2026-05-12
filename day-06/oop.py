class LogAnalyzer:

    def __init__(self, file_name):
        self.file_name  = file_name
        
    def read_file(self):
        with open(self.file_name, "r") as file:
            return file.readlines()

log1 = LogAnalyzer("app.log")
logs = log1.read_file()
print(logs)
