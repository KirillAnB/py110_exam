import json
import random
import faker

from conf import MODEL

TITLES = "BOOKS.txt" # Файл с заголовками книг

with open(TITLES, 'r', encoding='utf8') as file:
    data = file.readlines()


def get_title() -> str:
    '''
    Функция генерирует название книги
    :return: str
    '''
    result = random.choice(data).strip()
    return result


def get_year() -> int:
    '''
    Фнкция генерирует случайный год между 2000 и 2022
    :return: int
    '''
    year = random.randint(2000, 2022)
    return year


def get_pages() -> int:
    '''
    Фугкция генерирует колличество страниц в книге между 100 и 1000
    :return: int
    '''
    pages = random.randint(100, 1000)
    return pages


def get_isbn() -> str:
    '''
    Фугкция генерирует случайный isbn-номер
    :return: str
    '''
    my_fake = faker.Faker()
    isbn = my_fake.isbn13()
    return isbn


def get_rating() -> int:
    '''
    Фугкция генерирует случайный рейтинг для книги от 1 до 5
    :return: int
    '''
    rating = random.randint(1, 5)
    return rating


def get_price() -> float:
    '''
    Функция генерирует цену книги
    :return: float
    '''
    price = random.random() * random.randint(1000, 3000)
    return round(price, 2)


def get_authors() -> list:
    '''
    Функция генерирует список из двух авторов (RUS)
    :return: list
    '''
    fake_authors = faker.Faker("ru_RU")
    fake_authors_list = [fake_authors.name() for _ in range(2)]
    return fake_authors_list


def get_random_book(key=1) -> dict:
    '''
    Функция создает генератор словарей
    :param key: int
    :return: dict
    '''

    pk = key
    while True:
        random_book = {
            "model": MODEL,
            "pk": pk,
            "fields": {
                "title": get_title(),
                "year": get_year(),
                "pages": get_pages(),
                "isbn": get_isbn(),
                "rating": get_rating(),
                "price": get_price(),
                "author": get_authors()
            }}
        yield random_book
        pk += 1


def main():
    '''
    Основная функция программы, запускает создание генератора, создает 100 книг
    и записывает в файл формата json
    :return:
    '''
    random_books_generator = get_random_book()
    random_books_list = [next(random_books_generator) for _ in range(100)]
    with open("OUTPUT_BOOKS_FILE", "w", encoding="utf-8") as output_file:
        json.dump(random_books_list, output_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
