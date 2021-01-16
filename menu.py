import logging

from app import books

logger = logging.getLogger('scraper.menu')


USER_CHOICE = '''
Please enter one of the following

- 'b' to look at the best books
- 'c' to look at the cheapest books
- 'n' to just ge the next available book on the catalogue
- 'q' to exit

Enter your choice:
'''


def print_best_books():
    logger.info('Finding best books by rating...')
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding cheapest books...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)


def print_next_book():
    logger.info('Getting next book from generator')
    print(next(books_generator))


user_choices = {
    'b': print_best_books,
    'c': print_best_books,
    'n': print_next_book
}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Please input a valid option')
        user_input = input(USER_CHOICE)
    logger.debug('Terminating program.')


menu()
