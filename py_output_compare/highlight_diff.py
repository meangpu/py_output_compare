from normalize_output import normalize_output_no_lower


def highlight_diff(expect_input, got_input):

    if expect_input == got_input:
        return "no different found"

    norm_expect_input = normalize_output_no_lower(expect_input)
    norm_got_input = normalize_output_no_lower(got_input)

    final_word = []

    if norm_expect_input == norm_got_input:
        final_word.append(" 🀄 White space error!")

    else:
        max_len = max(len(norm_expect_input), len(norm_got_input))
        result = []

        result.append("diff>   👉[")

        for i in range(max_len):
            char1 = norm_expect_input[i] if i < len(norm_expect_input) else ""
            char2 = norm_got_input[i] if i < len(norm_got_input) else ""

            if char1 == char2:
                result.append(".")
            else:
                result.append("#")

        result.append("]")
        diff_result = "".join(result)
        final_word.append("-" * 80)
        final_word.append(diff_result)
        final_word.append(f"📩expect> [{norm_expect_input}]")
        final_word.append(f"🧒your's> [{norm_got_input}]")
        final_word.append(diff_result)

    final_word.append("-" * 80)
    final_word.append("💡 expect output: ")
    final_word.append(expect_input)
    final_word.append("-" * 80)
    final_word.append("📃 your output is:")
    final_word.append(got_input)
    final_word.append("~" * 80)
    final_output = "\n".join(final_word)
    return final_output


def main():
    print(highlight_diff("a" "asdfasdf", "adsfasdf"))


if __name__ == "__main__":
    main()
