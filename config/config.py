class TestData:
    TIMEOUT = 10
    SEARCH = "Dota 2"

    POLICY_PAGE_TEXT = "Дата изменения&nbsp;— 16 февраля 2022 г."




def read_file(filepath):
    with open(filepath, 'r') as file:
        words = file.readlines()
        return words
