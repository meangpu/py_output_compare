from py_output_compare.user_input_case import InputCase
from py_output_compare.highlight import highlight_diff
from py_output_compare.normalize_file_output import normalize_output
from py_output_compare.find_file import find_first_file
from py_output_compare.get_file_run_output import get_run_output_by_path


def get_compare_output_by__search_file_name(
    filename_1,
    filename_2,
    user_input_list=[InputCase("")],
    do_normalize_output=False,
    timeout=6,
    optional_file_name="",
):
    filepath_1 = find_first_file(filename_1)
    filepath_2 = find_first_file(filename_2)
    return get_compare_output_by_path(
        filepath_1,
        filepath_2,
        user_input_list,
        do_normalize_output,
        timeout,
        optional_file_name,
    )


def get_compare_output_by_path(
    file_path_1,
    file_path_2,
    user_input_list=[InputCase("")],
    do_normalize_output=False,
    timeout=6,
):
    result = []
    score = []
    result.append("=" * 80)

    for user_input in user_input_list:
        file_output_1 = get_run_output_by_path(
            file_path_1, user_input.case_input, timeout
        )
        file_output_2 = get_run_output_by_path(
            file_path_2, user_input.case_input, timeout
        )

        if do_normalize_output:
            file_output_2 = normalize_output(file_output_2)
            file_output_1 = normalize_output(file_output_1)

        if file_output_2 == file_output_1:
            result.append(f"✅: {user_input.case_name} pass!")
            score.append("🟢")

        else:
            result.append("~" * 80)
            result.append(f"❌: {user_input.case_name} fail!")
            score.append("🔴")
            result.append(highlight_diff(file_output_2, file_output_1))

    final_score = "".join(score)
    result.append("=" * 80)

    result.append(f"you got {final_score} scores")
    result.append("=" * 80)

    final_compare_result = "\n".join(result)
    return final_compare_result


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

    print(student_file)
    print(student_file_good)
    print(teacher_file)

    fail_student = get_compare_output_by_path(student_file, teacher_file, test_cases)
    pass_student = get_compare_output_by_path(
        student_file_good, teacher_file, test_cases
    )
    no_test_input = get_compare_output_by_path(student_file_good, teacher_file)

    print(fail_student)
    print(pass_student)
    print(no_test_input)

    print(get_compare_output_by__search_file_name("good.py", "bad.py"))
    print(get_compare_output_by__search_file_name("print_test.py", "print_test2.py"))


if __name__ == "__main__":

    main()
