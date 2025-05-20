from file_system import MiniFileSystem

fs = MiniFileSystem()

while True:
    print("\n=== Mini File System Emulator ===")
    print("1. Create File")
    print("2. Write File")
    print("3. Read File")
    print("4. Delete File")
    print("5. List Files")
    print("6. Truncate File")
    print("7. Show Disk Status")
    print("8. Show File Metadata")
    print("9. Save File System")
    print("10. Load File System")
    print("0. Exit")
    choice = input("Choose: ")

    if choice == '1':
        fname = input("File name: ")
        print(fs.create(fname))
    elif choice == '2':
        print("Available files:", fs.list_files())
        fname = input("File name: ")
        data = input("Data: ")
        print(fs.write(fname, data))
    elif choice == '3':
        print("Available files:", fs.list_files())
        fname = input("File name: ")
        print("Content:", fs.read(fname))
    elif choice == '4':
        print("Available files:", fs.list_files())
        fname = input("File name: ")
        print(fs.delete(fname))
    elif choice == '5':
        print("Files:", fs.list_files())
    elif choice == '6':
        fname = input("File name: ")
        print(fs.truncate(fname))
    elif choice == '7':
        fs.show_disk()
    elif choice == '8':
        fname = input("File name: ")
        print(fs.show_metadata(fname))
    elif choice == '9':
        print(fs.save_to_file())
    elif choice == '10':
        print(fs.load_from_file())        
    elif choice == '0':
        break
    else:
        print("Invalid choice.")
