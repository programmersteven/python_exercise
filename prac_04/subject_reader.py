"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    final = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        final.append(parts)
    print(final)
    input_file.close()
    subject_details(final)


def subject_details(final):
    for messages in final:
        print("{} is taught by {} and has {} students".format(messages[0], messages[1], messages[2]))


main()
