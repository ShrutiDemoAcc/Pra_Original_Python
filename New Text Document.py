# Open the file with read mode
with open('main.py', 'r') as file:
    lines = file.readlines()

# Remove '#' from each line and store in a new list
lines_without_comments = [line.replace('#', '') for line in lines]

# Open the file again in write mode and write the modified lines
with open('your_file.py', 'w') as file:
    file.writelines(lines_without_comments)
