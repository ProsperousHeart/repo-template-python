def str_func(input_str: str) -> str:
    """
    Returns a formatted string with the input.

    Args:
        input_str (str): The input string.

    Returns:
        str: A formatted string.
    Raises:
        TypeError: If input_str is None.
    """
    if input_str is None:
        raise TypeError("Input cannot be None")
    return f"You sent:  {input_str}"


def print_hi():
    print("Hi")


if __name__ == "__main__":
    print_hi()
