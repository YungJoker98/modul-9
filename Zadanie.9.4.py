from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Model książki
class Book(BaseModel):
    id: int
    title: str
    author: str
    pages: int
    cover_color: Optional[str] = None

# Przechowywanie książek w pamięci (dla uproszczenia)
books_db = []

@app.get("/books", response_model=List[Book])
def get_books(sort_by_pages: bool = False, cover_color: Optional[str] = None):
    books = books_db
    if cover_color:
        books = [book for book in books if book.cover_color == cover_color]
    if sort_by_pages:
        books = sorted(books, key=lambda book: book.pages)
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book)
def add_book(book: Book):
    books_db.append(book)
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books_db):
        if book.id == book_id:
            books_db[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    global books_db
    books_db = [book for book in books_db if book.id != book_id]
    return {"message": "Book deleted"}
