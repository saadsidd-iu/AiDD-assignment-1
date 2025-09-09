#import the book data from book_data.py
from book_data import books
from reviews_data import reviews

def load_data():
    """
    My thoughts: Very useful as it is able to complete my code for me, using my own entry as its instructions. Very convenient and easy.
    """
    return books

def add_book(self, bookId, title, aiMetric, releaseYear, author, genres, publisherName, location, pages, sales):
    """
    My understanding: This function creates a new dict that contains all of the fields.
    It then adds that dict to the books list with an "append".
    """   
    new_book = { 
        "bookId": bookId,
        "title": title,
        "aiMetric": aiMetric,
        "releaseYear": releaseYear,
        "author": author,
        "genres": genres,
        "publisher": {
            "publisherName": publisherName,
            "location": location
        },
        "pages": pages,
        "sales": sales
    }
    books.append(new_book)
    return new_book


def add_review(self, reviewId, reviewAuthor, reviewDate, reviewText, bookId):
    
    """
    Copilot prompt: No prompt, I started typing out the function and it auto completed it. Once I began to write the inputs required for the function it auto completed the rest.
    My understanding: This function creates a new dict that contains all of the fields.
    It then adds that dict to the reviews list with an "append". Very helpful, but only removed the extra "return" feature at the end of the suggestion.
    """   
    new_review = { 
        "reviewId": reviewId,
        "reviewAuthor": reviewAuthor,
        "reviewDate": reviewDate,
        "reviewText": reviewText,
        "bookId": bookId
    }
    reviews.append(new_review)
    return new_review


#create a function to save new data into the books and reviews lists
def save_data():
