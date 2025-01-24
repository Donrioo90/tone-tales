import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import Login from "./components/Login";
import Exercises from "./components/Exercises";
import Nutrition from "./components/Nutrition";

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/exercises" element={<Exercises />} />
        <Route path="/nutrition" element={<Nutrition />} />
      </Routes>
    </Router>
  );
};

export default App;
