import os
import random


def create_folder():
    folder_name = "files"

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    return folder_name


def create_files(folder_name):
    for i in range(1, 11):
        file_path = os.path.join(folder_name, f"file{i}.txt")

        with open(file_path, "w") as file:
            file.write(f"This is file {i}")


def count_files(folder_name):
    files = os.listdir(folder_name)
    return len(files)


def delete_half_files(folder_name):
    files = os.listdir(folder_name)

    half = len(files) // 2

    random_files = random.sample(files, half)

    for file in random_files:
        os.remove(os.path.join(folder_name, file))


def main():
    folder = create_folder()

    create_files(folder)

    print("Number of files before deleting:", count_files(folder))

    delete_half_files(folder)

    print("Number of files after deleting:", count_files(folder))


main()

     