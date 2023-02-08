import psutil


def extract_process_info(process) -> (str, dict | str):
    """ returns tuple of name and extracted process data """
    try:
        process_name = process.name()
        process_data = {
            "pid": process.pid,
            "cpu_percent": process.cpu_percent(),
            "ram_memory_percent": process.memory_percent(),
        }
        return process_name, process_data
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as exception:
        return str(exception), "exception"


def get_processes_info():
    result = (extract_process_info(process) for process in psutil.process_iter())
    return dict(result)
