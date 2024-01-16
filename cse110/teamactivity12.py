

largest_chapter = -1
largest_book = ""
largest_scripture = ""

with open("books_and_chapters.txt") as book_chapters:
    next(book_chapters, None)
    for book in book_chapters:
    
        clean_list = book.split(":")

        book = clean_list[0].strip()
        chapter = int(clean_list[1])
        what_testament = clean_list[2].strip()

        if what_testament == "Book of Mormon":

            if chapter > largest_chapter:

                largest_chapter = chapter
                largest_book = what_testament
                largest_scripture = book


print(largest_chapter)
print(largest_book)
print(largest_scripture)