with open("books.txt") as book_title:
    for line in book_title:
        book = line.strip()
        print(book)
        print("Goodbye")
print("The file is closed now")
