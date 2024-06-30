from py_output_compare import (
    normalize_output,
    normalize_output_no_lower,
)


def test_normalize_output():
    assert normalize_output(" Hello World \n") == "helloworld"
    assert normalize_output("  \tHello\nWorld\t ") == "helloworld"
    assert normalize_output("123 \t 456\n") == "123456"
    assert normalize_output("") == ""
    assert normalize_output("  ") == ""


def test_normalize_output_no_lower():
    assert normalize_output_no_lower(" Hello World \n") == "HelloWorld"
    assert normalize_output_no_lower("  \tHello\nWorld\t ") == "HelloWorld"
    assert normalize_output_no_lower("123 \t 456\n") == "123456"
    assert normalize_output_no_lower("") == ""
    assert normalize_output_no_lower("  ") == ""
