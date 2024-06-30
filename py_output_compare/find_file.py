import os


def find_files_recursively(filename, base_dir="./", case_sensitive=True, find_all=True):
    count = 0
    filename_lower = filename.lower() if not case_sensitive else None
    for root, _, files in os.walk(base_dir):
        for file in files:
            if (case_sensitive and file == filename) or (
                not case_sensitive and file.lower() == filename_lower
            ):
                full_path = os.path.join(root, file)
                count += 1
                yield full_path
                if not find_all:
                    print(f"{count} file found.")
                    return


def find_first_file_by_name(filename, folder_id):
    file_list = find_files_recursively(filename)
    for file in file_list:
        if folder_id in file:
            return file
    print("no file found")
    return None


def main():
    for file in find_files_recursively("Test.py"):
        print(file)

    print(find_first_file_by_name("Test.py", "py_output_compare"))


if __name__ == "__main__":
    main()
