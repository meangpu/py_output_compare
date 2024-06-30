import subprocess
from test_class import Test
from find_file import find_first_file_by_name
from highlight_diff import highlight_diff
from normalize_output import normalize_output


def get_score_emoji(score, max_score):
    result = []
    for i in range(max_score):
        if i < score:
            result.append("🟢")
        else:
            result.append("🔴")

    final_score = "".join(result)
    return final_score


def get_compare_to_teacher(student_file, file_name, input_data):
    teacher_file = find_first_file_by_name(file_name)
    return get_compare_output(student_file, teacher_file, input_data)


def get_run_output(filename, input_data, timeout_setting=6):
    output_lines = ""
    try:
        refactor_input = "\n".join((map(str, input_data)))
        result = subprocess.run(
            ["python", filename],
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


def get_compare_output(
    student, teacher_file, user_input_list, do_normalize_output=False
):
    result = []
    score = 0
    result.append("=" * 80)
    for user_input in user_input_list:
        teacher_output = get_run_output(teacher_file, user_input.case_input).strip()
        student_output = get_run_output(student, user_input.case_input).strip()

        if do_normalize_output:
            teacher_output = normalize_output(teacher_output)
            student_output = normalize_output(student_output)

        if teacher_output == student_output:
            result.append(f"✅: {user_input.case_name} pass!")
            score += 1
        else:
            result.append("~" * 80)
            result.append(f"❌: {user_input.case_name} fail!")
            result.append(highlight_diff(teacher_output, student_output))

    result.append("=" * 80)
    result.append(f"your got: {score} scores")
    result.append(f"{get_score_emoji(score, len(user_input_list))}")
    result.append("=" * 80)
    result.append("\n\n")

    final_compare_result = "\n".join(result)
    return final_compare_result


def main():
    teacher_file_name = "adder.py"
    student_file = find_first_file_by_name("to_evaluate.py", "to_evaluate.py")

    case1_input = [8.2, 1.8]
    case_input_int = [8.2, 999, 9334]

    test_cases = [
        Test(case1_input),
        Test(case_input_int),
    ]

    output = get_compare_to_teacher(student_file, teacher_file_name, test_cases)
    print(output)
    pass


if __name__ == "__main__":
    main()
