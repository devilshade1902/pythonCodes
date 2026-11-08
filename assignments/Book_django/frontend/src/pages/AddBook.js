import { useState } from "react";
import axios from "axios";

const AddBook = () => {
  const [book, setBook] = useState({
    title: "",
    author: "",
    publication_date: "",
    genre: "",
    description: "",
  });

  const token = localStorage.getItem("access_token");

  const handleChange = (e) => {
    setBook({ ...book, [e.target.name]: e.target.value });
  };

  const refreshToken = async () => {
    try {
      const refresh = localStorage.getItem("refresh_token");
      if (!refresh) return null;
  
      const response = await axios.post("http://localhost:8000/api/refresh/", {
        refresh,
      });
  
      const newAccessToken = response.data.access;
      localStorage.setItem("access_token", newAccessToken);
      return newAccessToken;
    } catch (error) {
      console.error("Failed to refresh token:", error.response?.data || error.message);
      return null;
    }
  };
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    let token = localStorage.getItem("access_token");
  
    if (!token) {
      alert("You must be logged in to add a book.");
      return;
    }
  
    try {
      const response = await axios.post(
        "http://localhost:8000/api/books/",
        book,
        {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        }
      );
  
      if (response.status === 201) {
        alert("Book added successfully!");
        setBook({ title: "", author: "", publication_date: "", genre: "", description: "" });
      }
    } catch (error) {
      if (error.response?.status === 401) {
        // If token is expired, try refreshing it
        const newToken = await refreshToken();
        if (newToken) {
          localStorage.setItem("access_token", newToken);
          handleSubmit(e); // Retry submission with the new token
        } else {
          alert("Session expired. Please log in again.");
        }
      } else {
        console.error("Error adding book:", error.response?.data || error.message);
        alert("Failed to add book. Please check input fields.");
      }
    }
  };
  return (
    <form onSubmit={handleSubmit}>
      <h1> Add Book </h1>
      <input type="text" name="title" value={book.title} onChange={handleChange} placeholder="Title" required />
      <input type="text" name="author" value={book.author} onChange={handleChange} placeholder="Author" required />
      <input type="date" name="publication_date" value={book.publication_date} onChange={handleChange} required />
      <input type="text" name="genre" value={book.genre} onChange={handleChange} placeholder="Genre" required />
      <textarea name="description" value={book.description} onChange={handleChange} placeholder="Description" required />
      <button type="submit">Add Book</button>
    </form>
  );
};

export default AddBook;
