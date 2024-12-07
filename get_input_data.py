import requests


def get_input_data(year: int, task_number: int) -> str:
    """
    Retrieves the input data from the adventofcode.com/{year}/day/{task_number}/input

    :param year: The year of the advent of code challenge
    :param task_number: The task number to retrieve the input data for
    :return: The input data as a string
    """
    session_cookie = open('cookie.txt', 'r').read()
    url = f'https://adventofcode.com/{year}/day/{task_number}/input'
    response = requests.get(url, cookies={'session': session_cookie})

    return response.text.strip()
