class LogAnalyzer:

    def __init__(self, file_name):
        self.file_name  = file_name
        
    def read_file(self):
        with open(self.file_name, "r") as file:
            return file.readlines()

    def analyze_file(self):
        count = 0
        with open(self.file_name, "r") as file:
            content = file.readlines()
            for text in content:
                if "INFO" in text:
                    count += 1
        return count

log1 = LogAnalyzer("app.log")

logs = log1.read_file()
print(logs)

count = log1.analyze_file()
print("INFO: ",count)
