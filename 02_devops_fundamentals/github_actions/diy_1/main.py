
def get_highest_number(numbers_list):
    """Returns the highest number of a list

    Args:
        numbers_list (list): list of numbers

    Returns:
        int: highest number of the list
    """
    return max(numbers_list)

if __name__ == "__main__":
    numbers_list = [10, 5, 9, 21, 45]

    highest = get_highest_number(numbers_list)
    print(highest)