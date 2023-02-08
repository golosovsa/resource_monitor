import psutil


def get_mutable_info():
    result = {
        "hdd_free_memory_mb": psutil.disk_usage("/").free / (1024 ** 2),
        "ram_free_memory_mb": psutil.virtual_memory().free / (1024 ** 2),
        "cpu_percent": psutil.cpu_percent(),
        "cpus_percent": psutil.cpu_percent(percpu=True),
    }
    return result
