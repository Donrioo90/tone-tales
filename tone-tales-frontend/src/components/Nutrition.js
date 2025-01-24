import React, { useEffect, useState } from "react";
import "./Nutrition.css";

const Nutrition = () => {
  const [nutritionTips, setNutritionTips] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/nutrition")
      .then((response) => response.json())
      .then((data) => setNutritionTips(data))
      .catch((error) => console.error("Error fetching nutrition tips:", error));
  }, []);

  return (
    <div className="nutrition">
      <h2>Nutrition Tips</h2>
      <ul>
        {nutritionTips.map((tip) => (
          <li key={tip.id}>{tip.advice}</li>
        ))}
      </ul>
    </div>
  );
};

export default Nutrition;
