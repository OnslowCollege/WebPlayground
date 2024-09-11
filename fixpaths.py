import os

def replace_text_in_file(target_text, file_path):
    # Get the directory containing the file
    folder_name = os.path.basename(os.getcwd())
    print(folder_name)

    # Read the file contents
    with open(file_path, 'r+') as file:
        file_contents = file.read()
        updated_contents = file_contents.replace(target_text, folder_name)
        print(updated_contents)
        file.write(updated_contents)

    print(f"Replaced '{target_text}' with '{folder_name}' in {file_path}")

# Example usage
file_path = f'{os.getcwd()}/.vscode/launch.json'
replace_text_in_file("SwiftTemplate", file_path)