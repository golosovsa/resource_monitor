import psutil
import platform
import socket
import uuid
from textwrap import wrap


def get_immutable_info() -> dict[str, str | int]:
    result = {
        "os_name": platform.system(),
        "os_version": platform.version(),
        "os_release": platform.release(),
        "cpu_physical": psutil.cpu_count(logical=False),
        "cpu_logical": psutil.cpu_count(logical=True),
        "ram_memory_mb": psutil.virtual_memory().total / (1024 ** 2),
        "hdd_memory_mb": psutil.disk_usage("/").total / (1024 ** 2),
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "mac": ":".join(wrap(f"{uuid.getnode():x}", 2)),
    }
    return result
