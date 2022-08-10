let url = `ws://${window.location.host}/ws/public-socket-server/`


const chatSocket = new WebSocket(url)

chatSocket.onmessage = (eve)=>{
    let data = JSON.parse(eve.data)

    if(data.type === 'public_chat'){
        console.log({data})
        const chatBox = document.querySelector('.chat-box');
        chatBox.insertAdjacentHTML('beforeend', `
        <p class="single-mssg"> 
            <img src="#" alt='#' /> 
            ${data.message} 
        </p>`)
    }

}


const form = document.querySelector('.mssg-frm')
form.addEventListener('submit', (eve)=>{
    eve.preventDefault();

    const message = eve.target.message.value
    chatSocket.send(JSON.stringify({
        'message': message
    }))

    form.reset();
})