from lib.list_of_books import list_of_books

def test_list_of_books_returns_list_with_one_book():
    actual = list_of_books(['ABC'])
    expected = ['ABC']

    assert actual == expected
    
def test_list_of_books_returns_list_with_three_books():
    actual = list_of_books(['Maximum Achievement', 'ABC','Smarter Investments'])
    expected = ['ABC', 'Maximum Achievement', 'Smarter Investments']

    assert actual == expected

def  test_list_of_books_returns_empty_list_message_when_empty_list_called():
    actual =  list_of_books([])
    expected = 'There were no books to sort!'

    assert actual == expected    