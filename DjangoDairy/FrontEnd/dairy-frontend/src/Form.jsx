import React, { useState } from "react";
import Header from "./Header";


const Form = () => {

    const [content, setContent] = useState("")
    const [flag, setFlag] = useState(false);



    const handleSubmit = async (eve) => {
        eve.preventDefault()
        const data = {
            content: content
        }
        const token = getCookie()
        const post = await fetch('http://localhost:8000/api/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': token
            },
            body: JSON.stringify(data)
        });
        console.log(post.status)
        if(post.status === 201){
            const pstMssg = await post.json()
            setFlag(true)
            setContent("")
            setTimeout(()=>{
                setFlag(false)
            }, 1000)
        }
        
    }

    return (
        <>
            <Header />
            <main className='container mr-4 flex-col'>
               {
                    flag &&
                    <div className='container pr-2 mssg'>
                        <p> Successfully Add to dairy </p>
                    </div>
               }
                <form className="frm" onSubmit={handleSubmit}>
                    <textarea
                        name="content"
                        id=""
                        cols="30"
                        rows="10"
                        value={content}
                        onChange={(eve) => { setContent(eve.target.value) }}
                    ></textarea>
                    <button type='submit' >Submit</button>
                </form>
            </main>
        </>
    )
}

export default Form;