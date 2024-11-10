import random

def read_student_ids(filename):
    """Reads student IDs from a file and returns them as a list."""
    try:
        with open(filename, 'r') as file:
            student_ids = [line.strip() for line in file if line.strip()]
        return student_ids
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []

def select_students_for_viva(student_ids):
    """Randomly selects students for viva, displaying each selection in order."""
    viva_counter = 1  # Counter to display the viva round
    remaining_students = student_ids[:]  # Make a copy of the list to modify

    while remaining_students:
        selected_student = random.choice(remaining_students)
        print(f"Viva #{viva_counter}: {selected_student}")
        remaining_students.remove(selected_student)
        viva_counter += 1

    print("\nAll students have been selected for viva.")
    return viva_counter

def main():
    # File name for student IDs
    filename = 'student_ids.txt'
    student_ids = read_student_ids(filename)

    if student_ids:
        while True:
            select_students_for_viva(student_ids)
            print("\nResetting student list for the next round...\n")
            input("Press Enter to start a new round of viva selections.\n")

if __name__ == "__main__":
    main()


