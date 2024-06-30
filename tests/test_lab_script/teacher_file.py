def sum_two_number():
    num1 = input("Enter a number:")
    num2 = input("Enter a number:")
    return f"{num1} + {num2} = {float(num1)+float(num2)}"


def main():
    print(sum_two_number())


if __name__ == "__main__":
    main()
