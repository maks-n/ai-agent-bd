import os
from config import MAX_CHARS

def get_files_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    file_content_string = ""
    try:
        with open(target_file, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > MAX_CHARS:
                file_content_string = f'{file_content_string[:MAX_CHARS]}...File "{file_path}" truncated at 10000 characters'
    except Exception as e:
        return f'Error: {e}'

    return file_content_string
