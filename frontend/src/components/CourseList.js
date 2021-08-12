import React from 'react';
import CourseItem from "./CourseItem"

const CourseList = ({courses}) => {
    return (
        <div>
            <h2>Список курсов</h2>
            {courses.map((course) =>
                <CourseItem course={course} key={course.id}/>
            )}

        </div>
    );
};
export default CourseList;