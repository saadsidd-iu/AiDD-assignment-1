"""
Copilot prompt: consolidate the data in book_data.py into a list
My thoughts: It automatically updated the file which was convenient and useful. It added a list around the sample data.
"""

books = [
    {
        "bookId": "1",
        "title": "The Quantum Garden",
        "aiMetric": "88",
        "releaseYear": "2023",
        "author": "Alice Johnson",
        "genres": ["Science Fiction", "Thriller"],
        "publisher": {
            "publisherName": "Bright Future Press",
            "location": "USA"
        },
        "pages": 420,
        "sales": [50000, 60000, 72000]
    },
    {
        "bookId": "2",
        "title": "The Forgotten Code",
        "aiMetric": "42",
        "releaseYear": "2024",
        "author": "Devon Chen",
        "genres": ["Mystery", "Techno-thriller"],
        "publisher": {
            "publisherName": "Redwood House",
            "location": "UK"
        },
        "pages": 310,
        "sales": [20000, 25000, 30000]
    },
    {
        "bookId": "3",
        "title": "Dreaming in Algorithms",
        "aiMetric": "65",
        "releaseYear": "2023",
        "author": "Sofia Martinez",
        "genres": ["Non-fiction", "Technology"],
        "publisher": {
            "publisherName": "AI4Books",
            "location": "Canada"
        },
        "pages": 280,
        "sales": [15000, 18000, 19000]
    }
]

def create_book(book_data):
    books.append(book_data)

def create_review(review_data):
    import importlib.util
    import sys
    import os
    file_path = os.path.join(os.path.dirname(__file__), 'reviews_data.py')
    spec = importlib.util.spec_from_file_location('reviews_data', file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules['reviews_data'] = module
    spec.loader.exec_module(module)
    module.reviews.append(review_data)
    with open(file_path, 'w') as f:
        f.write('reviews = ' + repr(module.reviews))