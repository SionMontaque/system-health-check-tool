from datetime import datetime
import os

def format_report(data):

    report = []
    report.append("=== System Health Report ===")
    report.append(f"Timestamp: {data['timestamp']}")
    report.append(f"Hostname: {data['hostname']}")
    report.append(f"OS: {data['os']}")
    report.append(f"CPU Usage: {data['cpu']}%")
    report.append(f"Memory Usage: {data['memory']}%")
    report.append(f"Disk Usage: {data['disk']}%")
    report.append(f"System Uptime: {data['uptime']}")


    return "\n".join(report)

def save_report(report_text):

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"system_report_{timestamp}.txt"

    report_path = os.path.join("reports", filename)

    with open(report_path, "w") as file:
        file.write(report_text)

    return report_path