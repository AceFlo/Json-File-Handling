import os


def create_files(num_files):
    file_name = "main_folder"
    if os.path.exists(file_name):
        pass
    else:
        os.mkdir(file_name)
    for i in range(1, num_files + 1):
        file_names = f"{file_name}/{i}.txt"
        with open(file_names, 'w') as f:

            f.write(f"This is file number {i}")
    print(f"{num_files} files created successfully.")


num_files = int(input("Enter the number of files to create: "))
create_files(num_files)

