# Define the file path
file_path = 'IndexingOfDramas1.txt'

# Read the file content
with open(file_path, 'r') as file:
    lines = file.readlines()

# Initialize a set to track drama names and a list for unique records
seen_dramas = set()
unique_lines = []

# Process each line
for line in lines:
    # Extract the drama name (second element after splitting by '*')
    drama_name = line.split('*')[1]

    # Check if the drama name has been seen before
    if drama_name not in seen_dramas:
        # If not, add the drama name to the set and the line to the unique list
        seen_dramas.add(drama_name)
        unique_lines.append(line)

# Write the unique lines back to the file
with open(file_path, 'w') as file:
    file.writelines(unique_lines)

print("Duplicates removed and file updated.")
