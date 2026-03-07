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
