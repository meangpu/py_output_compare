from py_output_compare.problem import Problem
import os


class Exercise:
    """topic is class that contain many exercise, use to evaluate all lab at once"""

    def __init__(self, exercise_name: str, problems: list[Problem]):
        self.exercise_name = exercise_name
        self.problems = problems

    def get_score_all_by_exercise(self) -> str:
        final_result = []
        for problem in self.problems:
            final_result.append("=" * 80)
            final_result.append(problem.problem_name)
            final_result.append("-" * 80)
            final_result.append(problem.get_score_all())
            final_result.append("=" * 80)
            final_result.append("\n")
        return "\n".join(final_result)

    def get_score_all_by_student_path_list(self, student_path_list: list[str]) -> str:
        """take around 20.34 second to complete all"""
        print("start evaluate student score...")
        final_result = []
        for student_path in student_path_list:
            exercise_path = os.path.join(student_path, self.exercise_name)
            for problem in self.problems:
                problem_path = os.path.join(exercise_path, problem.problem_name)

                final_result.append(problem.get_score_by_path(problem_path))
            final_result.append("=" * 80)
        return "\n".join(final_result)

    def get_score_id(self, student_id: str) -> str:
        final_result = []
        for problem in self.problems:
            final_result.append(problem.get_score_id(student_id))
        return "\n".join(final_result)

    def get_output_id(self, student_id: str) -> str:
        final_result = []
        for problem in self.problems:
            final_result.append(problem.get_output_id(student_id))
        return "\n".join(final_result)

    def print_score_all_by_exercise(self) -> None:
        for problem in self.problems:
            print(problem.problem_name)
            problem.print_score_all()
            print("=" * 80)

    def print_score_id(self, student_id: str) -> None:
        for problem in self.problems:
            problem.print_score_id(student_id)

    def print_output_id(self, student_id: str) -> None:
        for problem in self.problems:
            print(problem.get_output_id(student_id))

    def print_score_all_by_student_path_list(
        self, student_path_list: list[str]
    ) -> None:
        """take around 20.34 second to complete all"""
        for student_path in student_path_list:
            exercise_path = os.path.join(student_path, self.exercise_name)
            for problem in self.problems:
                problem_path = os.path.join(exercise_path, problem.problem_name)
                print((problem.get_score_by_path(problem_path)))
            print("=" * 80)

    def print_output_all_by_student_path_list(
        self, student_path_list: list[str]
    ) -> None:
        """take around 21 second to complete all"""
        for student_path in student_path_list:
            exercise_path = os.path.join(student_path, self.exercise_name)
            for problem in self.problems:
                problem_path = os.path.join(exercise_path, problem.problem_name)
                print((problem.print_output_by_path(problem_path)))
            print("=" * 80)

    def get_duplicate_file(
        self,
        folder_path="./",
        ignore_list=["TestRunner", "nattapong"],
        do_normalize=True,
        to_lowercase=True,
    ):
        result = []
        for problem in self.problems:
            result.append(
                problem.get_duplicate_file(
                    folder_path, ignore_list, do_normalize, to_lowercase
                )
            )
        return "\n".join(result)

    def get_exact_duplicate(
        self,
        folder_path="./",
        ignore_list=["TestRunner", "nattapong"],
    ):
        result = []
        for problem in self.problems:
            result.append(problem.get_exact_duplicate(folder_path, ignore_list))
        return "\n".join(result)

    def print_duplicate_report(self):
        for problem in self.problems:
            problem.print_duplicate_report()
