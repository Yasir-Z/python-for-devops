class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        
    def read_log(self):

        # open the file 
        with open(self.log_file) as file:

            # read the file 
            content = file.read()
   
        print(content)

    def count_info(self):
        with open(self.log_file, "r") as file:
            content = file.read()
            return content.count("INFO")
    
log = LogAnalyzer("app.log")
log.read_log()

print("INFO: ", log.count_info())
