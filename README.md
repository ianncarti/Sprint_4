# qa_python Sprint_4

| №  | Test name                                                      | Description                                                                                                                            |
|----|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 1  | test_add_new_book_add_two_books                                | Adds two books and checks that dict books_genre includes two items                                                                     |
| 2  | test_add_new_book_add_existing_book_does_not_duplicate         | Adds two books with same name and checks that dict books_genre contains only one of them                                               |
| 3  | test_add_new_book_add_books_with_wrong_name_length_not_in_dict | Adds two books with wrong name length and checks they are not in dict books_genre                                                      |
| 4  | test_set_book_genre_set_genre_for_new_book         | Adds new book, sets genre for added book and checks that genre appears in books_genre for added book                                   |
| 5  | test_set_book_genre_wrong_genre_cant_be_set         | Adds new book, sets wrong genre that not in genre list, then checks that genre not added for book in books_genre dict                  |
| 6  | test_get_books_with_specific_genre_gets_all_books_with_this_genre         | Adds two books with same genre and checks that method returns all of them with given genre                                             |
| 7  | test_get_books_with_specific_genre_add_book_with_different_genre_not_in_dict         | Adds book with genre 'Horror' and checks that this book will not return when method gets books with genre 'Comedy'                     |
| 8  | test_get_books_genre_returns_added_book         | Adds new book and checks that method returns this book                                                                                 |
| 9  | test_get_books_for_children_add_two_books_filters_book_with_age_rating         | Adds two books, one of them with age rating genre and checks that book with age rating genre not in list for kids                      |
| 10 | test_add_book_in_favorites_add_existing_book         | Adds new book then adds this book to Favorites list, then checks new books is in Favorites list                                        |
| 11 | test_add_book_in_favorites_add_not_existing_book_wont_appear_in_favorites         | Adds book that not in books_genre dict and checks that this book not in Favorites list                                                 |
| 12 | test_delete_book_from_favorites         | Adds new book, then adds this book to Favorites, then deletes this book from Favorites and checks that this book not in Favorites list |
| 13 | test_get_list_of_favorites_books_returns_added_book         | Adds new book, then adds this book to Favorites list and checks that this books in Favorites list                                      |