# Open the file 
my_file = open("app.log", "r")

# file_read
file_read = my_file.readlines()

# show content
def count_words():
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for text in file_read:
        for key in counts:
            if key in text:
                counts[key] += 1
    
    print(counts)

count_words()

# close file
my_file.close()
