import os, sys, re

def get_usable_path(path):
    """
    Checks the directory for other folders with the same name.\n
    Returns a unique path, with a number appended to the end: (n)
    """
    original_path = path
    counter = 0
    while os.path.exists(path) and counter < 99999:
        path = original_path + '(' + str(counter) + ')'
        counter += 1
    return path

def send_to_folder():
    del sys.argv[0] #Delete script run from arguments.
    if os.path.exists(sys.argv[0]):
        # Get file name from file path.
        file_name = re.findall(r"[^\\]*$", sys.argv[0])[0]
        # Get directory path from file path.
        current_directory = re.findall(r".*\\", sys.argv[0])[0]
        # Create new directory, with the first files name.
        new_directory = os.path.join(current_directory, file_name.split('.')[0])
        if os.path.exists(new_directory):
            # Check if the created directory already exists, if it does, get unique path.
            new_directory = get_usable_path(new_directory)
        os.mkdir(new_directory)

    for file_path in sys.argv:
        # Get file name from file path.
        file_name = re.findall(r"[^\\]*$", file_path)[0]
        file_directory = os.path.join(new_directory, file_name)
        os.rename(file_path, file_directory)

if __name__ == "__main__":
    send_to_folder()
