import re

from task1 import load, extract_mul_data,MUL_REGEX


DO_DONT_REGEX = r"do\(\)|don't\(\)"


def dummy_data() -> str:
    """
    Return a dummy data string
    """
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def extract_commands(data: str) -> list[str]:
    """
    Extract all the commands from the data
    """
    return re.findall(MUL_REGEX + r"|" + DO_DONT_REGEX, data)


def execute_commands(commands: list[str]) -> int:
    """
    Execute all the commands and return the sum of the multiplication operations
    """
    total_sum = 0
    active = True
    for command in commands:
        if "do()" in command:
            active = True
        elif "don't()" in command:
            active = False
        elif active:
            num1, num2 = extract_mul_data(command)
            total_sum += num1 * num2
    return total_sum


def main():
    data = load("input.txt")
    # data = dummy_data()
    commands = extract_commands(data)
    total_sum = execute_commands(commands)
    print(total_sum)


if __name__ == "__main__":
    main()