def normalize_output(output):
    return output.strip().lower().replace("\n", "").replace(" ", "").replace("\t", "")


def normalize_output_no_lower(output):
    return output.strip().replace("\n", "").replace(" ", "").replace("\t", "")


def main():
    print(normalize_output(" Hello World , pro gram to work but not to feel!\n"))
    print(
        normalize_output_no_lower(
            " Hello World , pro gram to work but not to feel!\n no t even sure that this is real "
        )
    )
    pass


if __name__ == "__main__":
    main()
