from health_checks import (get_hostname, get_os_info, get_cpu_usage, get_memory_usage, get_disk_usage, get_system_uptime, get_top_processes)
from utils import format_report, save_report
from datetime import datetime

def main():
    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hostname": get_hostname(),
        "os": get_os_info(),
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "uptime": get_system_uptime(),
        "processes": get_top_processes()
    }

    report = format_report(data)

    print(report)

    report_path = save_report(report)

    print(f"\nReport saved to: {report_path}")


if __name__ == "__main__":
    main()    