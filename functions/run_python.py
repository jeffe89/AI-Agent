import os
import subprocess

def run_python_file(working_directory, file_path, args=None):

    # Get absolute path of directory
    abs_working_dir = os.path.abspath(working_directory)

    # Check if filepath is outside the working directory
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    # Check if file path does not exist
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    # Check if file path is not a Python file
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    # Execute python file with subprocess.run
    try:
        commands = ["python3", abs_file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_dir,
        )

        # Capture output
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        # Check for return codes other than 0
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    
    # Return error and state exception if encountered
    except Exception as e:
        return f"Error: executing Python file: {e}"

        