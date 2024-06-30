from py_output_compare import (
    find_first_file,
    InputCase,
    get_compare_output_by_path,
)


def main():
    student_file = find_first_file("bad.py")
    student_file_good = find_first_file("good.py")
    teacher_file = find_first_file("teacher_file.py")

    case1_input = [8.2, 1.8]
    case_input_int = [8.2, 999, 9334]

    test_cases = [
        InputCase(case1_input),
        InputCase(case_input_int),
    ]

    print(teacher_file)

    fail_student = get_compare_output_by_path(student_file, teacher_file, test_cases)
    pass_student = get_compare_output_by_path(
        student_file_good, teacher_file, test_cases
    )
    no_test_input = get_compare_output_by_path(student_file_good, teacher_file)

    print(fail_student)
    print(pass_student)
    print(no_test_input)


if __name__ == "__main__":

    main()
