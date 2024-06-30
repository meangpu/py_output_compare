from py_output_compare.find_file import find_files
from py_output_compare import get_score_emoji, get_compare_output, InputCase

print(get_score_emoji(20, 20))
case1_input = [8.2, 1.8]
case_input_int = [8.2, 999, 9334]

test_cases = [
    InputCase(case1_input),
    InputCase(case_input_int),
]

print(get_compare_output("bad.py", "good.py", test_cases))

print(find_files("find_test.txt"))
