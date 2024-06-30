from unittest.mock import patch


def base_test_user_input(expect_input, expect_output, main):
    with patch("builtins.input", side_effect=expect_input), patch(
        "builtins.print"
    ) as mock_print:
        try:
            main()
        except SystemExit:
            pass
        output_calls = [call[0][0] for call in mock_print.call_args_list]
        assert output_calls == expect_output
