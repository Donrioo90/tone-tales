import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./index.css";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import Nutrition from "./components/Nutrition";
import Login from "./components/Login";

const App = () => {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/nutrition" element={<Nutrition />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    </Router>
  );
};

ReactDOM.render(<App />, document.getElementById("root"));
