import subprocess
from py_output_compare.user_input_case import InputCase
from py_output_compare.highlight import highlight_diff
from py_output_compare.normalize_file_output import normalize_output
from py_output_compare.get_score import get_score_emoji
from py_output_compare.find_file import find_first_file


def get_run_output_by_search_file_name(filename, input_data, timeout_setting=6):
    """_summary_

    Args:
        filename (_type_): get file name instead of path, it will try to find by itself
        input_data (_type_):
        timeout_setting (int, optional):. Defaults to 6.
    """
    path = find_first_file(filename)
    return get_run_output_by_path(path, input_data, timeout_setting)


def get_run_output_by_path(file_path, input_data, timeout_setting=6):
    output_lines = ""
    try:
        refactor_input = "\n".join((map(str, input_data)))
        result = subprocess.run(
            ["python", file_path],
            input=refactor_input,
            capture_output=True,
            text=True,
            timeout=timeout_setting,
            encoding="utf-8",
        )
        output_lines = result.stdout
        output_lines += result.stderr

        if len(output_lines) == 0:
            raise Exception("your file give no output")

        return output_lines
    except EOFError:
        output_lines += "🔚 End of file Error"
        return output_lines
    except subprocess.TimeoutExpired:
        output_lines += "💀 Timed out!!!"
        return output_lines
    except Exception as e:
        output_lines += f"😲 Encountered an exception: {str(e)}"
        return output_lines


def get_compare_output_by__search_file_name(
    filename_1,
    filename_2,
    user_input_list=[InputCase("")],
    do_normalize_output=False,
):
    filepath_1 = find_first_file(filename_1)
    filepath_2 = find_first_file(filename_2)
    return get_compare_output_by_path(
        filepath_1, filepath_2, user_input_list, do_normalize_output
    )


def get_compare_output_by_path(
    file_path_1,
    file_path_2,
    user_input_list=[InputCase("")],
    do_normalize_output=False,
):
    result = []
    score = 0
    result.append("=" * 80)
    for user_input in user_input_list:
        file_output_1 = get_run_output_by_path(file_path_1, user_input.case_input)
        file_output_2 = get_run_output_by_path(file_path_2, user_input.case_input)

        if do_normalize_output:
            file_output_2 = normalize_output(file_output_2)
            file_output_1 = normalize_output(file_output_1)

        if file_output_2 == file_output_1:
            result.append(f"✅: {user_input.case_name} pass!")
            score += 1
        else:
            result.append("~" * 80)
            result.append(f"❌: {user_input.case_name} fail!")
            result.append(highlight_diff(file_output_2, file_output_1))

    result.append("=" * 80)
    result.append(f"your got: {score} scores")
    result.append(f"{get_score_emoji(score, len(user_input_list))}")
    result.append("=" * 80)
    result.append("\n\n")

    final_compare_result = "\n".join(result)
    return final_compare_result


def main():
    # student_file = find_first_file("bad.py")
    # student_file_good = find_first_file("good.py")
    # teacher_file = find_first_file("teacher_file.py")

    # case1_input = [8.2, 1.8]
    # case_input_int = [8.2, 999, 9334]

    # test_cases = [
    #     InputCase(case1_input),
    #     InputCase(case_input_int),
    # ]

    # print(student_file)
    # print(student_file_good)
    # print(teacher_file)

    # fail_student = get_compare_output_by_path(student_file, teacher_file, test_cases)
    # pass_student = get_compare_output_by_path(
    #     student_file_good, teacher_file, test_cases
    # )
    # no_test_input = get_compare_output_by_path(student_file_good, teacher_file)

    # print(fail_student)
    # print(pass_student)
    # print(no_test_input)

    print(get_compare_output_by__search_file_name("good.py", "bad.py"))


if __name__ == "__main__":

    main()
