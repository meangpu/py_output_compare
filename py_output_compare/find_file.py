import os


def find_files(filename, base_dir="./", case_sensitive=True, find_all=True):
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
    print("*" * 105)
    print(f"{count} file{'s' if count != 1 else ''} found.")
    print("*" * 105)


def find_first_file(filename, base_dir="./", case_sensitive=True):
    filename_lower = filename.lower() if not case_sensitive else None
    for root, _, files in os.walk(base_dir):
        for file in files:
            if (case_sensitive and file == filename) or (
                not case_sensitive and file.lower() == filename_lower
            ):
                full_path = os.path.join(root, file)
                print("File found.")
                return full_path
    print("No file found.")
    return None


def find_first_file_contain_id(filename, folder_id):
    file_list = find_files(filename)
    for file in file_list:
        if folder_id in file:
            return file
    print("no file found")
    return None


def main():
    for file in find_files("test_class.py"):
        print(file)

    print(find_first_file_contain_id("test_class.py", "py_output_compare"))
    print(find_first_file("test_class.py"))


if __name__ == "__main__":
    main()
