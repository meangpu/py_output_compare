from py_output_compare.compare_file import get_compare_output_by_path, get_score_by_path
from py_output_compare.user_input_case import InputCase
from py_output_compare.find_file import find_files, find_first_file_contain_id


class Exercise:
    def __init__(
        self,
        lab_name,
        input_cases=[InputCase("")],
        do_normalize_input=False,
        timeout_setting=6,
        teacher_name="manee-2024",
    ):
        self.lab_name = lab_name
        self.input_cases = input_cases
        self.do_normalize_input = do_normalize_input
        self.teacher_name = teacher_name
        self.timeout_setting = timeout_setting

    # def print_output_all_student(self):
    #     teacher_file_path = find_first_file_contain_id(self.lab_name, self.teacher_name)
    #     all_student = find_files(self.lab_name)

    #     for student_file_path in all_student:
    #         print("\n")
    #         print("-" * 80)
    #         print(student_file_path)
    #         print(
    #             get_compare_output_by_path(
    #                 student_file_path,
    #                 teacher_file_path,
    #                 self.input_cases,
    #                 self.do_normalize_input,
    #                 self.timeout_setting,
    #             ),
    #         )
    #         print(student_file_path)
    #         print("-" * 80)
    #         print("\n")

    def get_output_id(self, student_id):
        student_file_path = find_first_file_contain_id(self.lab_name, student_id)
        teacher_file_path = find_first_file_contain_id(self.lab_name, self.teacher_name)
        result = get_compare_output_by_path(
            student_file_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
        )
        return result

    def get_score_id(self, student_id):
        teacher_file_path = find_first_file_contain_id(self.lab_name, self.teacher_name)
        student_file_path = find_first_file_contain_id(self.lab_name, student_id)

        score_num, score_emoji = get_score_by_path(
            student_file_path,
            teacher_file_path,
            self.input_cases,
            self.do_normalize_input,
            self.timeout_setting,
        )

        final_score_output = f"{score_num} {score_emoji} {student_file_path}"
        return final_score_output
