import os, sys, re

def get_usable_path(path):
    original_path = path
    counter = 0
    while os.path.exists(path) and counter < 100:
        path = original_path + '(' + str(counter) + ')'
        counter += 1
    return path

def main():
    del sys.argv[0]

    if os.path.exists(sys.argv[0]):
        file_name = re.findall(r"[^\\]*$", sys.argv[0])[0]
        current_directory = re.findall(r".*\\", sys.argv[0])[0]
        new_directory = os.path.join(current_directory, file_name.split('.')[0])
        if os.path.exists(new_directory):
            new_directory = get_usable_path(new_directory)
        os.mkdir(new_directory)

    for file_path in sys.argv:
        file_name = re.findall(r"[^\\]*$", file_path)[0]
        file_directory = os.path.join(new_directory, file_name)
        os.rename(file_path, file_directory)

        


if __name__ == "__main__":
    main()
