import re

def sort_markdown_by_location(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Extract the header and separator lines
    header = lines[0]
    separator = lines[1]

    # Process the data lines
    data_lines = lines[2:]

    # Parse each line into a list of columns and keep the original line for writing back
    parsed_lines = []
    for line in data_lines:
        columns = line.split('|')
        if len(columns) > 5:  # Ensure the line has enough columns
            location = columns[3].strip()  # Location is in the 4th column (0-indexed)
            parsed_lines.append((location, line))

    # Sort the list by location
    sorted_lines = sorted(parsed_lines, key=lambda x: x[0])

    # Write the sorted lines back to a new file
    with open(output_file, 'w') as file:
        file.write(header)
        file.write(separator)
        for _, line in sorted_lines:
            file.write(line)

# Usage
sort_markdown_by_location('summer_24_internships_simplify_list_filtered.md', 'summer_24_internships_simplify_list_filtered_sorted.md')
