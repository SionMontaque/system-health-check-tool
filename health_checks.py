import platform
import socket
import psutil


def get_hostname():
    hostname = socket.gethostname()
    return hostname


def get_os_info():
    os_name = platform.system()
    os_version = platform.version()
    return f"{os_name} {os_version}"


def get_cpu_usage():
    try:
        return psutil.cpu_percent(interval=1)
    except Exception as e:
        return f"Error retrieving CPU usage: {e}"


def get_memory_usage():
    try:
        memory = psutil.virtual_memory()
        return memory.percent
    except Exception as e:
        return f"Error retrieving memory usage: {e}"


def get_disk_usage():
    try:
        disk = psutil.disk_usage('/')
        return disk.percent
    except Exception as e:
        return f"Error retrieving disk usage: {e}"


from datetime import datetime
def get_system_uptime():

    try:
        boot_time = psutil.boot_time()

        boot_time_datetime = datetime.fromtimestamp(boot_time)
        current_time = datetime.now()

        uptime_delta = current_time - boot_time_datetime

        days = uptime_delta.days
        hours = uptime_delta.seconds // 3600
        minutes = (uptime_delta.seconds % 3600) // 60

        return f"{days} days, {hours} hours, {minutes} minutes"

    except Exception as e:
        return f"Error retrieving uptime: {e}"



