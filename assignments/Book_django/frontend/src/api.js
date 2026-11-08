import axios from "axios";

const API_URL = "http://localhost:8000/api/";

export const register = (userData) => axios.post(`${API_URL}register/`, userData);
export const login = (userData) => axios.post(`${API_URL}token/`, userData);
export const getBooks = (token) => axios.get(`${API_URL}books/`, { headers: { Authorization: `Bearer ${token}` } });
export const getBook = (id, token) => axios.get(`${API_URL}books/${id}/`, { headers: { Authorization: `Bearer ${token}` } });
export const addBook = (bookData, token) => axios.post(`${API_URL}books/`, bookData, { headers: { Authorization: `Bearer ${token}` } });
export const updateBook = (id, bookData, token) => axios.put(`${API_URL}books/${id}/`, bookData, { headers: { Authorization: `Bearer ${token}` } });
export const deleteBook = (id, token) => axios.delete(`${API_URL}books/${id}/`, { headers: { Authorization: `Bearer ${token}` } });
