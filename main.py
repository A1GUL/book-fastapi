from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    price: float
    is_available: bool
    category: str
    id: int

books = []

@app.get("/")
def home():
    return {"message": "Book API"}

@app.post("/books")
def create_book(book: Book):
    books.append(book)
    return book

@app.get("/books")
def get_books():
    return books

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}

    return {"message": "Book not found"}