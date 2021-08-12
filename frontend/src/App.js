import React, {useEffect, useState} from "react";
import CourseList from "./components/CourseList";

import axios from "axios"

function App() {
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        fetchCourses();
    }, [])

    function fetchCourses() {
        axios.get('/api/course/').then((response) => {
            setCourses(response.data);
        });
    }

    return (<div>
        <h1>Добро пожаловать.</h1>
        <CourseList courses={courses}/>
    </div>);
}

export default App;
