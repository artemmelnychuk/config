import subprocess
import os

def run_black_on_directory(directory_path, line_length=88, check=False, diff=False):
    """
    Run Black on the specified directory.
    
    :param directory_path: Path to the directory to format
    :param line_length: Maximum line length for Black
    :param check: If True, don't write the files back, just return the status
    :param diff: If True, print the diff for the fixed files
    :return: True if successful, False otherwise
    """
    try:
        cmd = ["black", directory_path, f"--line-length={line_length}"]
        if check:
            cmd.append("--check")
        if diff:
            cmd.append("--diff")
        
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Black: {e}")
        print(e.stdout)
        print(e.stderr)
        return False
    except FileNotFoundError:
        print("Black is not installed or not in the system PATH")
        return False
