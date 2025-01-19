import sys
import os

def is_running_as_executable():
    # Check if the application is running in a frozen state
    if getattr(sys, 'frozen', False):
        # Running as an executable
        return True
    else:
        # Running as a script
        return False

if __name__ == "__main__":
    if is_running_as_executable():
        input("Running as an executable.")
        # Get the path of the executable
        exe_path = os.path.dirname(sys.executable)
        input(f"Executable path: {exe_path}")
    else:
        input("Running as a script.")
        # Get the path of the script
        script_path = os.path.dirname(os.path.realpath(__file__))
        input(f"Script path: {script_path}")