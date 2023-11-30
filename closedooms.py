import psutil

process_name = "chocolate-doom.exe"

for proc in psutil.process_iter():
    try:
        # Check if process name matches
        if process_name in proc.name():
            proc.terminate()  # Terminate the process
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass