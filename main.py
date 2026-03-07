from health_checks import (get_hostname, get_os_info, get_cpu_usage, get_memory_usage)

def main():
    print("System Health Report")
    
    hostname = get_hostname()
    os_info = get_os_info()
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()

    print(f"Hostname: {hostname}")
    print(f"OS: {os_info}")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")

if __name__ == "__main__":
    main()    