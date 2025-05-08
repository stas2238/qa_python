from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_adds_book_with_valid_name(self):
        collector = BooksCollector()


        collector.add_new_book('Недоросль')
        assert 'Недоросль' in collector.get_books_genre() and collector.get_books_genre()['Недоросль'] == ''

    def test_add_new_book_does_not_add_duplicate(self):
        collector = BooksCollector()


        collector.add_new_book('Метро 2033')
        collector.add_new_book('Метро 2033')
        assert list(collector.get_books_genre().keys()).count('Метро 2033') == 1

    def test_add_new_book_does_not_add_long_name(self):
        collector = BooksCollector()


        long_name = 'X' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_set_book_genre_sets_genre_if_book_exists_and_genre_valid(self):
        collector = BooksCollector()


        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'

    def test_set_book_genre_does_nothing_if_book_not_exists(self):
        collector = BooksCollector()


        collector.set_book_genre('Неизвестная книга', 'Ужасы')
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_set_book_genre_does_nothing_if_genre_invalid(self):
        collector = BooksCollector()


        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Фэнтези')
        assert collector.get_book_genre('Колобок') == ''

    def test_get_book_genre_returns_none_for_unknown_book(self):
        collector = BooksCollector()


        assert collector.get_book_genre('Неизвестная книга') is None

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()


        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Фантастика')
        assert set(collector.get_books_with_specific_genre('Фантастика')) == {'Книга1', 'Книга2'}

    def test_get_books_with_specific_genre_returns_empty_list_for_invalid_genre(self):
        collector = BooksCollector()


        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фэнтези') == []

    def test_get_books_genre_returns_books_genre_dict(self):
        collector = BooksCollector()


        collector.add_new_book('Книга1')
        assert isinstance(collector.get_books_genre(), dict)

    def test_get_books_for_children_returns_only_child_friendly_books(self):
        collector = BooksCollector()


        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Мультфильмы')
        collector.set_book_genre('Книга2', 'Ужасы')
        assert collector.get_books_for_children() == ['Книга1']

    def test_add_book_in_favorites_adds_book_if_exists(self):
        collector = BooksCollector()


        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        assert 'Книга1' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_does_not_add_if_not_exists(self):
        collector = BooksCollector()


        collector.add_book_in_favorites('Несуществующая')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_does_not_add_duplicate(self):
        collector = BooksCollector()


        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга1')
        assert collector.get_list_of_favorites_books().count('Книга1') == 1

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()


        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        collector.delete_book_from_favorites('Книга1')
        assert 'Книга1' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_does_nothing_if_not_in_favorites(self):
        collector = BooksCollector()


        collector.add_new_book('Книга1')
        collector.delete_book_from_favorites('Книга1')  # не было в избранном
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_list(self):
        collector = BooksCollector()


        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        assert isinstance(collector.get_list_of_favorites_books(), list)
