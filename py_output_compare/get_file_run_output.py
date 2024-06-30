import subprocess
from py_output_compare.user_input_case import InputCase
from py_output_compare.find_file import find_first_file


def get_run_output_by_search_file_name(
    filename, input_data=[InputCase("")], timeout_setting=6
):
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
