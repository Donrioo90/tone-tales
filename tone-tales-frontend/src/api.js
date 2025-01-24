import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

export const login = (credentials) => axios.post(`${API_URL}/login`, credentials);
export const getExercises = () => axios.get(`${API_URL}/exercises`);
export const getNutrition = () => axios.get(`${API_URL}/nutrition`);
