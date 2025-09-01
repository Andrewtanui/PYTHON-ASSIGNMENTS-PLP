# File Read & Write Challenge with Error Handling
filename = input("Enter the filename to read: ")
try:
    with open(filename, 'r') as infile:
        content = infile.read()
    modified_content = content.upper()  # Example modification: convert to uppercase
    new_filename = f"modified_{filename}"
    with open(new_filename, 'w') as outfile:
        outfile.write(modified_content)
    print(f"Modified content written to {new_filename}")
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Could not read the file.")
