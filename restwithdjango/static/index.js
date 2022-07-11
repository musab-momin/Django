/*
this is for csrf token 
I get this from django official site

*/

let isEditing = false
const text = document.getElementById('task');
let updateId = null

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const todoParent = document.querySelector('.todo__list');


const fetchTasks = async () => {
    const response = await fetch('http://127.0.0.1:8000/todo/task-list')
    const data = await response.json()

    todoParent.innerHTML = ''
    data.forEach(ele => {
        todoParent.innerHTML += `
        <li class="todo__item">
                <label for="todo-1">
                    <span class="check__box" id = ${ele.id} onclick='handleComplete(${ele.id})'>
                        <i class="far fa-check check__pointer"></i>
                    </span>
                    <span class="item__title tasks" id = ${ele.id}>${ele.title}</span>
                </label>
            <i 
            class="fas fa-trash-alt item__trash-can" 
            style='color: green'
            id='${ele.id}' 
            onclick='handleUpdate(this.id)'
            >Edit</i>
      </li>`
    })
}

const makeCallToApi = async (url) =>{

    const csrftoken = getCookie('csrftoken');
    let data = {
        title: text.value,
        completed: false
    }
    

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    })
    const responseData = await response.json()
    fetchTasks()
    text.value = ""
    isEditing = false
    updateId = null

}

const handleSubmit = async (eve) => {
    console.log('working');
    eve.preventDefault()
    const urlToCall = isEditing ? `http://127.0.0.1:8000/todo/update-task/${updateId}` : 'http://127.0.0.1:8000/todo/create-task'
    makeCallToApi(urlToCall)
}

const handleUpdate = (id) =>{
    isEditing = true
   
    const taskList = document.querySelectorAll('.tasks')
    for (ele of taskList){
       if (ele.id === id){
           updateId = ele.id
           text.value = ele.innerHTML
       }   
    }


}

const handleComplete = async (id)=>{
    console.log(id);
    const deleteUrl = `http://127.0.0.1:8000/todo/delete-task/${id}`
    const response = await fetch(deleteUrl)
    const responseData = await response.json()
    fetchTasks() 
}

window.onload = () => {
    
    fetchTasks()

    form = document.querySelector('.frm')
    form.addEventListener('submit', handleSubmit)

}