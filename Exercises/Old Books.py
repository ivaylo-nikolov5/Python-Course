searched_book = input()

books_count = 0

next_book = input()
is_book_found = False

while next_book != "No More Books":
    if next_book == searched_book:
        print(f"You checked {books_count} books and found it.")
        is_book_found = True
        break

    books_count += 1
    next_book = input()

if not is_book_found:
    print(f"The book you search is not here!\nYou checked {books_count} books.")