import platform
import socket
import psutil

def get_hostname():
    hostname = socket.gethostname()
    return hostname

def get_os_info():
    os_name = platform.system()
    os_version = platform.release()
    return f"{os_name} {os_version}"

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

from datetime import datetime
def get_system_uptime():
    boot_time = psutil.boot_time()
    boot_time_datetime = datetime.fromtimestamp(boot_time)

    current_time = datetime.now()
    uptime = current_time - boot_time_datetime
    return uptime

def get_top_processes(limit=3):
    processes = []

    for proc in psutil.process_iter(['name', 'cpu_percent']):
        try:
            processes.append((proc.info['name'], proc.info['cpu_percent']))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(key=lambda x: x[1], reverse=True)
    
    return [proc[0] for proc in processes[:limit]]

