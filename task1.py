import re


MUL_REGEX = r"mul\(\d{,3},\d{,3}\)"


def load(filename: str) -> str:
    """
    Load the content of the file and return it as a string
    """
    with open(filename, "r") as fileobj:
        return fileobj.read()


def dummy_data() -> str:
    """
    Return a dummy data string
    """
    return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def extract_mul_str(data: str) -> list[str]:
    """
    Extract all the multiplication operations from the data
    """
    return re.findall(MUL_REGEX, data)


def extract_mul_data(mut_str: str) -> tuple[int, int]:
    """
    Extract the two numbers from the multiplication string
    """
    content = re.findall(r"\d{1,3}", mut_str)
    return int(content[0]), int(content[1])


def main():
    data = load("input.txt")
    # data = dummy_data()
    mul_list = extract_mul_str(data)
    total_sum = 0
    for mul_str in mul_list:
        num1, num2 = extract_mul_data(mul_str)
        total_sum += num1 * num2
    print(total_sum)



if __name__ == "__main__":
    main()