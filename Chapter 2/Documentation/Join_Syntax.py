books = "The Hitchhiker's Guide to the Galaxy"
bookList = list(books)

print(bookList[0:3])

print(''.join(bookList[0:3]))
## The join() method takes all items in an iterable and joins them into one string
## expected output = The

print(''.join(bookList[-6:]))
## expected output = Galaxy