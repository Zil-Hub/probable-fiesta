from functions import read_file, process_line, write_output


def main():
    # Input and output file names
    input_file = "students.txt"  # Example input file
    output_file = "emails.txt"  # Example output file

    try:
        # Step 1: Read input file
        lines = read_file(input_file)

        # Step 2: Process each line to generate the corresponding email address
        processed_lines = [process_line(line) for line in lines]

        # Step 3: Write output to a new file
        write_output(output_file, processed_lines)
        print(f"Emails have been successfully written to {output_file}.")

    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()
