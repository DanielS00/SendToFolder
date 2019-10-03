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
    """Creates a folder, and moves selected files into it."""
    # Delete script run from arguments.
    del sys.argv[0]

    if os.path.exists(sys.argv[0]):
        # Cut file name from file path.
        file_name = re.findall(r"[^\\]*$", sys.argv[0])[0]

        # Cut the directory location of file from file path.
        current_directory = re.findall(r".*\\", sys.argv[0])[0]

        # Create the path for the new folder.
        new_directory = os.path.join(current_directory, file_name.split('.')[0])

        # Check if folder already exists, if it does, get a path which doesn't.
        if os.path.exists(new_directory):
            new_directory = get_usable_path(new_directory)
        
        # Create folder.
        os.mkdir(new_directory)

    # Move selected files to the created folder.
    for file_path in sys.argv:
        file_name = re.findall(r"[^\\]*$", file_path)[0]
        file_directory = os.path.join(new_directory, file_name)
        os.rename(file_path, file_directory)

if __name__ == "__main__":
    send_to_folder()
