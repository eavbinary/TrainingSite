import React, {useEffect, useState} from "react";
import CourseList from "./components/CourseList";
import Modal from "./components/Modal/Modal";
import axios from "axios"
import "./App.css"

function App() {
    const [courses, setCourses] = useState([]);
    const [modalContact, setModalContact] = useState(false);

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
        <div className="contact">
            <a href="#" onClick={() => {setModalContact(true);}}>Контакты</a>
        </div>
        <Modal active={modalContact} setActive={setModalContact}>
            <h1>Контакты</h1>
            Какие то данные для связи.
        </Modal>
    </div>);
}

export default App;
