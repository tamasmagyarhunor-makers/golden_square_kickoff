```python
"""
As a user
so I can see a list of books alphabetically
I want to be able to so sort a list of books
"""
# Parameters:
# - list_of_books eg. ['Maximum Achivement', 'ABC','Smarter Investments']
# sort_books(list_of_books)
# Returns:
# - list eg.  ['ABC', 'Maximum Achievement', 'Smarter Investments']
# Side effects:
# - None

# Examples:
def test_list_of_books_with_one_book():

    assert list_of_books(['ABC']) == ['ABC']

def test_list_of_books_with_three_books():
    assert list_of_books(['Maximum Achievement', 'ABC','Smarter Investments']) == ['ABC', 'Maximum Achievement', 'Smarter Investments']


```

