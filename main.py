from file_system import MiniFileSystem

fs = MiniFileSystem()

while True:
    print("\n=== Mini File System Emulator ===")
    print("1. Create File")
    print("2. Write File")
    print("3. Read File")
    print("4. Delete File")
    print("5. List Files")
    print("0. Exit")
    choice = input("Choose: ")

    if choice == '1':
        fname = input("File name: ")
        print(fs.create(fname))
    elif choice == '2':
        fname = input("File name: ")
        data = input("Data: ")
        print(fs.write(fname, data))
    elif choice == '3':
        fname = input("File name: ")
        print("Content:", fs.read(fname))
    elif choice == '4':
        fname = input("File name: ")
        print(fs.delete(fname))
    elif choice == '5':
        print("Files:", fs.list_files())
    elif choice == '0':
        break
    else:
        print("Invalid choice.")
