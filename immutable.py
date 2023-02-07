import psutil
import platform


def get_immutable_info() -> dict[str, str | int]:
    result = {
        "os_name": platform.system(),
        "os_version": platform.version(),
        "os_release": platform.release(),
        "cpu_physical": psutil.cpu_count(logical=False),
        "cpu_logical": psutil.cpu_count(logical=True),
        "memory_mb": psutil.virtual_memory().total / (1024 ** 2),
    }
    return result
