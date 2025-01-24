import React from "react";
import "./Home.css";

const Home = () => {
  return (
    <div className="home">
      <h2>Welcome to Tone Tales</h2>
      <p>
        Take care of your body. It's the only place you have to live.
      </p>
      <img
        src="https://via.placeholder.com/500"
        alt="Gym"
        className="home-image"
      />
      <p>Even a short workout is better than not exercising at all.</p>
    </div>
  );
};

export default Home;
