import csv
import time

UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

SUBJECT_LIST = ["Maths", "Science", "English", "Computer", "Physics", "Chemistry"]
TOTAL_STUDENT_COUNT = 150


def generate_name(student_number):
    value = student_number + int(time.time())

    first_name = (
        UPPERCASE_LETTERS[value % 26]
        + LOWERCASE_LETTERS[value % 26] * 4
    )
    last_name = (
        UPPERCASE_LETTERS[(value + 5) % 26]
        + LOWERCASE_LETTERS[(value + 3) % 26] * 5
    )

    return first_name + " " + last_name


def main():
    current_time_seed = int(time.time())
    file_name = "students_" + str(current_time_seed) + ".csv"

    with open(file_name, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["ID", "Name", "Subject", "Marks"])

        for student_number in range(1, TOTAL_STUDENT_COUNT + 1):
            student_id = "S" + format(student_number, "03")

            name = generate_name(student_number)

            subject_index = (student_number + current_time_seed) % len(SUBJECT_LIST)
            subject_name = SUBJECT_LIST[subject_index]

            marks_value = (student_number * (current_time_seed % 10 + 1)) % 101

            writer.writerow([student_id, name, subject_name, marks_value])

    print("CSV file created successfully:", file_name)


if __name__ == "__main__":
    main()