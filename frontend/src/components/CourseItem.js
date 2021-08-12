import React from 'react';

const CourseItem = (props) => {
    let url = "/course/" + props.course.id ;
    return (
        <div>
            <a href={url}>
                <strong>{props.course.name}</strong>
            </a><br/>

            &nbsp;&nbsp;&nbsp;
            {props.course.description}

            <br/><br/>
        </div>
    );
};

export default CourseItem;