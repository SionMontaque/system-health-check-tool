from health_checks import (get_hostname, get_os_info, get_cpu_usage, get_memory_usage, get_disk_usage, get_system_uptime, get_top_processes)

def main():
    print("System Health Report")
    
    hostname = get_hostname()
    os_info = get_os_info()
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    uptime = get_system_uptime()
    processes = get_top_processes()

    print(f"Hostname: {hostname}")
    print(f"OS: {os_info}")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage}%")
    print(f"System Uptime: {uptime}")

    print("\nTop Processes:")
    for i, process in enumerate(processes, start=1):
        print(f"{i}. {process}")

if __name__ == "__main__":
    main()    