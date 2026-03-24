import csv
import sys


def main():

    # TODO: Check for command-line usage
    from sys import argv

    if len(argv) != 3:
        print('Usage: python dna.py database/file.csv sequence/text.txt')
        return False

    # TODO: Read database file into a variable
    rows = []
    with open(argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(argv[2], 'r', encoding="utf-8") as f:
        dna = f.read()

    # TODO: Find longest match of each STR in DNA sequence

    # Create a list to store the longest matchs of the dna, acoording to the number of strs in the database file
    l_m = []
    for i in range((len(reader.fieldnames)) - 1):
        l_m.append(longest_match(dna, (reader.fieldnames[i+1])))

    # TODO: Check database for matching profiles
    # Loop through each row
    for row in rows:
        # Create a list to store the str numbers of each row
        name_row = []
        for i in range((len(reader.fieldnames)) - 1):
            name_row.append(int(row[reader.fieldnames[i+1]]))

        # If the row is equal to the dna list, print the name and break
        if name_row == l_m:
            print(f'{row['name']}')
            break
    # If didn't print and break, print no match
    else:
        print('No match')

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
