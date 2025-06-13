from src.utils.logger import create_logger, func_wrapper, sol_wrapper, logging


log_obj = create_logger(file_name="Template_Repo", file_mode="w")

# @func_wrapper
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
        log_obj.error("str_func called with None input.")
        raise TypeError("Input cannot be None")
    log_obj.debug("str_func called with input_str='%s'", input_str)
    return f"You sent:  {input_str}"


# @func_wrapper
def print_hi():
    log_obj.info("print_hi called.")
    print("Hi")

# @sol_wrapper
def main():
    """
    Main function to execute the script.
    """
    print_hi()
    # try:
    #     result = str_func("Hello, World!")
    #     logger.info("str_func result: %s", result)
    # except TypeError as e:
    #     logger.error("Error in str_func: %s", e)
    str_func("Hello, World!")
    log_obj.warning("This is the end!")
    log_obj.critical("This is a critical message, but not an error.")
    log_obj.error("This is an error message, but not an exception.")


if __name__ == "__main__":
    main()
