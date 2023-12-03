import re

def is_open(application_link):
    return '🔒' not in application_link

def is_ca_or_remote(location):
    return 'CA' in location or 'Remote' in location

def process_markdown(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Skip the header and separator lines
    data_lines = lines[2:]

    filtered_listings = []
    for line in data_lines:
        columns = line.split('|')
        if len(columns) > 5:  # Ensure the line has enough columns
            company, role, location, application_link, date_posted = [col.strip() for col in columns[1:6]]
            if is_open(application_link) and is_ca_or_remote(location):
                filtered_listings.append(line)

    with open(output_file, 'w') as file:
        # Write the header and separator lines
        file.write(lines[0] + lines[1])
        # Write the filtered listings
        for listing in filtered_listings:
            file.write(listing)

# Usage
process_markdown('summer_24_internships_simplify_list.md', 'summer_24_internships_simplify_list_filtered.md')
