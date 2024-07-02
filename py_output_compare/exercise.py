from py_output_compare.problem import Problem


class Exercise:
    """topic is class that contain many exercise, use to evaluate all lab at once"""

    def __init__(self, exercise_name: str, problems: list[Problem]):
        self.exercise_name = exercise_name
        self.problems = problems

    def get_score_all_exercise(self) -> str:
        final_result = []
        for problem in self.problems:
            final_result.append(problem.problem_name)
            final_result.append(problem.get_score_all())
            final_result.append("=" * 80)
        return "\n".join(final_result)

    def print_score_all_exercise(self) -> None:
        for problem in self.problems:
            print(problem.problem_name)
            problem.print_score_all()
            print("=" * 80)

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
