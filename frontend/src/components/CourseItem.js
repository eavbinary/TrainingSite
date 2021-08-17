import React, {useEffect, useState} from "react";
import Modal from "./Modal/Modal";

const CourseItem = (props) => {
    const [modalActive, setModalActive] = useState(false);
    const [modalActiveRec, setModalActiveRec] = useState(false);

    return (
        <div>
            <a href="#" onClick={() => {
                setModalActive(true);
            }}><strong>{props.course.name}</strong></a>
            <br/>
            <Modal active={modalActive} setActive={setModalActive}>
                <h1>{props.course.name}</h1>
                {props.course.description}
                <br/><br/>
                <center>
                    <button onClick={() => {
                        setModalActive(false);
                        setModalActiveRec(true);
                    }}> Записаться на курс
                    </button>
                </center>
            </Modal>
            <Modal active={modalActiveRec} setActive={setModalActiveRec}>
                <h1>Запись на курс {props.course.name}<br/></h1>
                <form>
                    ФИО:
                    <input/><br/>
                    eMail:
                    <input/><br/><br/>
                    <center><button onClick={() => {setModalActiveRec(false)}}>Отправить</button></center>
                </form>
            </Modal>
        </div>

    );

};

export default CourseItem;