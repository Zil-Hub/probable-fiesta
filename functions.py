import os


def read_file(filename):
    """Reads the input file and returns a list of lines."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")

    with open(filename, 'r') as file:
        lines = file.readlines()

    return lines


def process_line(line):
    """Process a single line and return the corresponding email address."""
    # Split the line into UCAS number and name
    ucas_number, name = line.strip().split(' ', 1)

    # Split the name into first and last name parts
    last_name, first_names = name.split(', ')
    first_names = first_names.split(' ')

    # Create the email address
    email_parts = [first_names[0].lower()]  # First name initial
    for name in first_names[1:]:
        email_parts.append(name[0].lower())  # Other name initials

    email = f"{'.'.join(email_parts)}{ucas_number[-4:]}@poppleton.ac.uk"

    return f"{ucas_number} {email}"


def write_output(filename, lines):
    """Write the processed lines to an output file."""
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')
