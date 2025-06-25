import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_len_name_is_8_add(self, collector):
        book_name = 'Парфюмер'
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book_name', ['', 'Клуб любителей книг и пирогов из картофельных очистков'])
    def test_add_new_book_len_name_is_None_or_54_not_add(self, collector,book_name):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_success(self, collector):
        book_name = '1984'
        collector.add_new_book(book_name)
        genre = 'Фантастика'
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    def test_get_book_genre_existing_book(self, collector):
        book_name = 'Парфюмер'
        collector.add_new_book(book_name)
        genre = 'Роман'
        collector.books_genre[book_name] = genre
        assert collector.get_book_genre(book_name) == genre

    def test_add_book_in_favorites_added(self, collector):
        book_name = 'Парфюмер'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_books_with_specific_genre_age_rating(self, collector):
        book_name_specific_genre = ['Оно','Шерлок Холмс']
        genre_specific = ['Ужасы','Детективы']
        collector.add_new_book(book_name_specific_genre)
        collector.set_book_genre(book_name_specific_genre, genre_specific)
        specific_genre = collector.get_books_genre[book_name_specific_genre]
        assert len(collector.get_books_with_specific_genre()) == 2

    def test_delete_book_from_favorites(self, collector):
        book_name = 'Шерлок Холмс'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        favorite = collector.get_list_of_favorites_books
        collector.delete_book_from_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_books_for_children_not_age_rating(self, collector):
        genre_age_rating = ['Ужасы', 'Детективы']
        books_for_children = 'Маугли'
        collector.add_new_book(books_for_children)
        genre = 'Мультфильмы'
        collector.set_book_genre(books_for_children, genre)
        assert collector.get_books_for_children not in genre_age_rating

    def test_get_list_of_favorites_books_list(self, collector):
        collector.add_new_book('Парфюмер')
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Парфюмер')
        collector.add_book_in_favorites('Шерлок Холмс')
        assert len(collector.get_list_of_favorites_books()) == 2

