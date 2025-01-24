import React, { useState, useEffect } from "react";
import axios from "axios";

const Exercises = () => {
    const [exercises, setExercises] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:5000/exercises")
            .then(response => setExercises(response.data))
            .catch(error => console.error("Error fetching exercises:", error));
    }, []);

    return (
        <div>
            <h1>Exercises</h1>
            {exercises.map(exercise => (
                <div key={exercise.id}>
                    <h2>{exercise.title}</h2>
                    <p>{exercise.description}</p>
                    <img src={exercise.image_url} alt={exercise.title} />
                </div>
            ))}
        </div>
    );
};

export default Exercises;
