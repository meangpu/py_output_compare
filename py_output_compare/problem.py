from py_output_compare.compare_file import (
    get_compare_output_by_path,
    get_score_by_path,
    print_compare_output_by_path,
)
from py_output_compare.find_file import (
    find_files,
    find_first_file_contain_id,
    find_first_file,
)
from py_output_compare.test_case import TestCase


class Problem:
    def __init__(
        self,
        problem_name,
        input_cases=[TestCase("")],
        do_normalize_input=False,
        timeout_setting=6,
        teacher_name="manee-2024",
    ):
        self.problem_name = problem_name
        self.input_cases = input_cases
        self.do_normalize_input = do_normalize_input
        self.teacher_name = teacher_name
        self.timeout_setting = timeout_setting

    def get_score_all(self) -> str:
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        all_student = find_files(self.problem_name)
        result = []

        for student_file_path in all_student:
            score_num, score_emoji = get_score_by_path(
                student_file_path,
                teacher_file_path,
                self.input_cases,
                self.do_normalize_input,
                self.timeout_setting,
            )

            final_score_output = f"{score_num} {score_emoji} {student_file_path}"
            result.append(final_score_output)
        return "\n".join(result)

    def get_output_id(self, student_id) -> str:
        student_file_path = find_first_file_contain_id(self.problem_name, student_id)
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        result = get_compare_output_by_path(
            student_file_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
        )
        return result

    def get_output_from_upload_file(self, upload_file_name="to_evaluate.py") -> str:
        student_file_path = find_first_file(upload_file_name)
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        result = get_compare_output_by_path(
            student_file_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
            score_web_format=True,
        )
        return result

    def get_score_id(self, student_id) -> str:
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        student_file_path = find_first_file_contain_id(self.problem_name, student_id)

        score_num, score_emoji = get_score_by_path(
            student_file_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
        )

        final_score_output = f"{score_num} {score_emoji} {student_file_path}"
        return final_score_output

    def print_score_id(self, student_id) -> None:
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        student_file_path = find_first_file_contain_id(self.problem_name, student_id)

        score_num, score_emoji = get_score_by_path(
            student_file_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
        )

        print(f"{score_num} {score_emoji} {student_file_path}")

    def print_score_all(self) -> None:
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        all_student = find_files(self.problem_name)

        for student_file_path in all_student:
            score_num, score_emoji = get_score_by_path(
                student_file_path,
                teacher_file_path,
                self.input_cases,
                self.do_normalize_input,
                self.timeout_setting,
            )

            print(f"{score_num} {score_emoji} {student_file_path}")

    def print_output_id(self, student_id) -> None:
        student_file_path = find_first_file_contain_id(self.problem_name, student_id)
        teacher_file_path = find_first_file_contain_id(
            self.problem_name, self.teacher_name
        )
        print_compare_output_by_path(
            student_file_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
        )
