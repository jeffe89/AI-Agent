import os
from google.genai import types

def get_files_info(working_directory, directory=None):

    # Get absolute path of directory
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir

    # Check if directory is outside the working directory
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    # Check if directory argument is not a directory
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    # Attempt to gather file contents of target directory
    try:
        files_info = []
        
        # Loop through each file is directory
        for filename in os.listdir(target_dir):
            
            # Get file path
            filepath = os.path.join(target_dir, filename)

            # Check if directory
            is_dir = os.path.isdir(filepath)

            # gather file_size 
            file_size = 0
            file_size = os.path.getsize(filepath)

            # Append to files_info list
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)

    # Return error and state exception if encountered
    except Exception as e:
        return f'Error listing files: {e}'

# Schema for getting file information
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)