"""BookWorm"""
def main():
    """BookWorm"""
    books = []
    time_count = 0
    book = 0
    for _ in range(int(input())) :
        time_limit = float(input())
        for i in range(int(input())) :
            books.append(float(input()))
        books.sort()
        for i in books :
            time_count += i
            if time_count <= time_limit :
                book += 1
        print(book)
        book,time_count = 0, 0
        books.clear()
main()
