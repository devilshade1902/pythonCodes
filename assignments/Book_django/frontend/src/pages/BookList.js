// src/components/BookList.js
import { useState, useEffect } from "react";

const BookList = () => {
  const [books, setBooks] = useState([]);
  const token = localStorage.getItem("access_token");

  useEffect(() => {
    const fetchBooks = async () => {
      const response = await fetch("http://127.0.0.1:8000/books/", {
        headers: { Authorization: `Bearer ${token}` },
      });

      if (response.ok) {
        const data = await response.json();
        setBooks(data);
      } else {
        console.log("Failed to fetch books");
      }
    };

    fetchBooks();
  }, [token]);

  return (
    <div>
      <h2>Book List</h2>
      <ul>
        {books.map((book) => (
          <li key={book.id}>{book.title} by {book.author}</li>
        ))}
      </ul>
    </div>
  );
};

export default BookList;
