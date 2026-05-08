import psutil 

def cpu_utilization():
    
    cpu_threshold = int(input("Enter CPU utilization: "))
    
    current_cpu = psutil.cpu_percent(interval=1)

    print(current_cpu)

    disk_usage = psutil.disk_usage('/')

    print("The disk usage is: ", disk_usage)
    

    p = psutil.Process()

    print(p.memory_info())

    if current_cpu > cpu_threshold:
    
        print("Alert email have been sent")
    else:
        print("CPU utilization is safe")

cpu_utilization()
