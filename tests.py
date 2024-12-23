import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, books_collector):

        # добавляем две книги
        books_collector.add_new_book('Гордость и предубеждение и зомби')
        books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(books_collector.get_books_genre()) == 2

    def test_add_new_book_add_existing_book_does_not_duplicate(self, books_collector):

        # добавляем 2 одинаковые книги
        books_collector.add_new_book('Гордость и предубеждение и зомби')
        books_collector.add_new_book('Гордость и предубеждение и зомби')

        # проверяем, что добавилась одна
        assert len(books_collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['', '111111111111111111111111111111111111111111'])
    def test_add_new_book_add_books_with_wrong_name_length_not_in_dict(self, name, books_collector):

        # добавляем книги с названиями не подходящими под условие 0 < len(name) < 41:
        books_collector.add_new_book(name)

        # проверяем, что книги не добавились в словарь
        assert len(books_collector.get_books_genre()) == 0

    def test_set_book_genre_set_genre_for_new_book(self, books_collector):

        # добавляем новую книгу
        books_collector.add_new_book('Гордость и предубеждение и зомби')

        # устанавливаем добавленной книге жанр ужасы
        books_collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        # проверяем, что жанр добавился к новой книге
        assert books_collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_wrong_genre_cant_be_set(self, books_collector):

        # добавляем новую книгу
        books_collector.add_new_book('Гордость и предубеждение и зомби')

        # устанавливаем добавленной книге жанр, которого нет в списке допустимых жанров
        books_collector.set_book_genre('Гордость и предубеждение и зомби', 'Преколы')

        # проверяем, что жанр остался пустым
        assert books_collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Зов Ктулху'])
    def test_get_books_with_specific_genre_gets_all_books_with_this_genre(self, books_collector, name):
        # создаём книги через параметризацию
        books_collector.add_new_book(name)

        # устанавливаем каждой созданной книге жанр ужасы
        books_collector.set_book_genre(name, 'Ужасы')

        # проверяем, что обе книги выдаются при выводе по жанру "Ужасы"
        assert 'Гордость и предубеждение и зомби', 'Зов Ктулху' in books_collector.get_books_with_specific_genre('Ужасы')

    def test_get_books_with_specific_genre_add_book_with_different_genre_not_in_dict(self, books_collector):
        # добавляем новую книгу
        books_collector.add_new_book('Гордость и предубеждение и зомби')

        # устанавливаем добавленной книге жанр ужасы
        books_collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert 'Гордость и предубеждение и зомби' not in books_collector.get_books_with_specific_genre('Комедии')

    def test_get_books_genre_returns_added_book(self, books_collector):

        # добавили новую книгу
        books_collector.add_new_book('Гордость и предубеждение и зомби')

        # создали переменную с ожидаемым результатом
        expected_dict = {'Гордость и предубеждение и зомби': ""}

        # сохранили в переменную результат работы проверяемого метода
        result = books_collector.get_books_genre()

        # проверяем совпадение ожидаемого результата с фактическим
        assert expected_dict == result


    @pytest.mark.parametrize('name, genre', [
        ['Гордость и предубеждение и зомби','Ужасы'],
        ['Двенадцать стульев', 'Комедии']
    ])
    def test_get_books_for_children_add_two_books_filters_book_with_age_rating(self, books_collector, name, genre):
        # создаём 2 книги через параметризацию, одна из них имеет жанр не для детей
        books_collector.add_new_book(name)

        # устанавливаем каждой созданной книге жанр
        books_collector.set_book_genre(name, genre)

        # создали переменную, в которую сохраним отфильтрованный список с книгами для детей
        result = books_collector.get_books_for_children()

        # проверяем, что книга с жанром "Ужасы" не попала в список с книгами для детей
        if genre == 'Ужасы':
            assert name not in result
        elif genre == 'Комедии':
            assert name in result

    def test_add_book_in_favorites_add_existing_book(self, books_collector):
        # добавили новую книгу
        books_collector.add_new_book('Гордость и предубеждение и зомби')

        # добавили созданную книгу в Избранное
        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        # проверяем, что книга находится в списке избранных
        assert 'Гордость и предубеждение и зомби' in books_collector.favorites

    def test_add_book_in_favorites_add_not_existing_book_wont_appear_in_favorites(self, books_collector):
        # добавили в Избранное книгу, которой нет в словаре books_genre
        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        # проверяем, что книга не добавилась в Избранное
        assert 'Гордость и предубеждение и зомби' not in books_collector.favorites

    def test_delete_book_from_favorites(self, books_collector):
        # добавили новую книгу
        books_collector.add_new_book('Гордость и предубеждение и зомби')

        # добавили созданную книгу в Избранное
        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        # удаляем книгу из Избранное
        books_collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        # проверяем, что книга отсутствует в списке Избранное
        assert 'Гордость и предубеждение и зомби' not in books_collector.favorites

    def test_get_list_of_favorites_books_returns_added_book(self, books_collector):
        # добавили новую книгу
        books_collector.add_new_book('Гордость и предубеждение и зомби')

        # добавили созданную книгу в Избранное
        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        # создали переменную с ожидаемым результатом
        expected_list = ['Гордость и предубеждение и зомби']

        # сохранили в переменную результат работы проверяемого метода
        result = books_collector.get_list_of_favorites_books()

        # проверяем совпадение ожидаемого результата с фактическим
        assert expected_list == result
