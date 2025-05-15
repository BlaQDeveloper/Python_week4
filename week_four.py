try:
    with open("week_four.txt", "r") as file:
        lines = file.read()
        modified_text = lines.upper()
    with open("modified.txt", "w") as modified_file:
        modified_file.write(modified_text)
except FileNotFoundError:
    print("The file was not found.")