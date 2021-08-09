import axios from 'axios';

function createToken(user, password) {
    
    axios({
        method: 'POST',
        url: '/api/token/',
        data: {
            "username": user,
            "password": password
        }
    })
        .then((response) => {
            if (response.status == 200) {
                localStorage.setItem('token', response.data.access);
            }
            else {
                localStorage.setItem('token', '');
            }
        });
}

function useAxios() {
    //Так делать не нужно, сделано для управщения решения задачи
    //В следущих уроках будет переделано.
    createToken('admin', 'j6v-58s-KpZ-NBA');
    let token = localStorage.getItem('token');

    axios({
        method: 'GET',
        url: '/api/people/',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
        .then((response) => {
            if (response.status == 200) {
                response.data.forEach(element => {
                    console.log(element);    
                });
                
            }
        })
        .catch((err) => {

        });

}

function useFetch() {
    fetch('/api/course/')
        .then((response) => {
            if (!response.ok) {
                throw new Error("Ошибка доступа к данным.");
            }
            return response.json();
        })
        .then((data) => {
            console.log();
            let result_course = document.getElementById('tb_course');
            let res = "";
            for (let index = 0; index < data.length; index++) {
                res += "<a href=\"/course/" + data[index].id + "\">" + data[index].name + "</a><br>";
                res += "&nbsp;&nbsp;&nbsp;";
                res += data[index].description + "<br><br>";
            }
            result_course.innerHTML = res;
        })
        .catch((err) => {
            let result_course = document.getElementById('tb_course');
            result_course.innerHTML = err.message;
        })
}


useFetch();
useAxios();

