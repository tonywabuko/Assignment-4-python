def process_file():
    try:
        # Ask the user for the input filename
        filename = input("Enter the name of the file to read: ")

        # Attempt to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (convert text to uppercase)
        modified_content = content.upper()

        # Create a new filename for the output
        output_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(output_filename, "w") as file:
            file.write(modified_content)

        # Success message
        print(f"✅ Processing complete! The modified file is saved as '{output_filename}'.")

    except FileNotFoundError:
        print(" Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print(" Error: Permission denied. You don't have access to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

# Run the function
process_file()

# This code will prompt the user for a filename, read its content, modify it, and save it to a new file.
