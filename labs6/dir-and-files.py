import os
import string

def list_contents(path):
    if os.path.exists(path):
        print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
        print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        print("All:", os.listdir(path))
    else:
        print("Path does not exist.")

def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

def check_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")

def count_lines(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print("Number of lines:", sum(1 for line in file))
    else:
        print("File does not exist.")

def write_list_to_file(filename, lst):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')
    print(f"List written to {filename}")

def generate_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is file {letter}.txt")
    print("26 files created.")

def copy_file(source, destination):
    if os.path.exists(source):
        with open(source, 'r') as src, open(destination, 'w') as dest:
            dest.write(src.read())
        print("File copied successfully.")
    else:
        print("Source file does not exist.")

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted successfully.")
        else:
            print("No write permission to delete the file.")
    else:
        print("File does not exist.")


while True:
    print("\nSelect an action:")
    print("1. Show directories and files")
    print("2. Check access to a path")
    print("3. Check if a path exists")
    print("4. Count the number of lines in a file")
    print("5. Write a list to a file")
    print("6. Generate 26 text files (A-Z)")
    print("7. Copy a file")
    print("8. Delete a file")
    print("9. Exit")

    choice = input("Enter the operation number: ")

    if choice == '1':
        path = input("Enter the path: ")
        list_contents(path)
    elif choice == '2':
        path = input("Enter the path: ")
        check_access(path)
    elif choice == '3':
        path = input("Enter the path: ")
        check_path(path)
    elif choice == '4':
        filename = input("Enter the file path: ")
        count_lines(filename)
    elif choice == '5':
        filename = input("Enter the filename: ")
        lst = input("Enter a list of values separated by commas: ").split(',')
        write_list_to_file(filename, lst)
    elif choice == '6':
        generate_files()
    elif choice == '7':
        source = input("Enter the source file: ")
        destination = input("Enter the destination file: ")
        copy_file(source, destination)
    elif choice == '8':
        path = input("Enter the file path to delete: ")
        delete_file(path)
    elif choice == '9':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")