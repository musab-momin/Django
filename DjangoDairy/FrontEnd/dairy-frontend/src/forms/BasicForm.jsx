import React from "react"
import { useState } from "react"

const BasicForm = ()=>{
    
    const [frm, setFrm] = useState({name: '',email: '', password: '', termsConditions: true})

    const handleChange = (eve)=>{
        let {name, value} = eve.target
        
        if (name === 'termsConditions'){
            setFrm((prev)=>{
                
                if(value === 'false')   value = true
                else if (value === 'true')  value = false

                return {...prev, [name]: value}
            })
        }


        else{
            setFrm((prev)=>{
                return {...prev, [name]: value}
            })  
        }
        
    }


    const handleSubmit = (eve)=>{
        eve.preventDefault()
    }
   
    return(<>

        <form onSubmit={handleSubmit} className="frm">
            <input 
            type="text" 
            placeholder="name"
            name="name"
            value={frm.name}
            onChange={handleChange}
            />
            <input 
            type="email" 
            placeholder="email"
            name="email"
            value={frm.email} 
            onChange={handleChange}
            />
            <input 
            type="password" 
            placeholder="password"
            name="password"
            value={frm.password} 
            onChange={handleChange}
            />
            <input 
            type="checkbox" 
            name="termsConditions"
            value={frm.termsConditions} 
            checked = {frm.termsConditions}
            onChange={handleChange}
            />
            
            <button type="submit">Submit</button>
        </form>
        <div className="container">
            <h2>welcome { frm.name } </h2>
            <p>Please verify your {frm.email} email </p>
        </div>
        
    </>)
}



export default BasicForm