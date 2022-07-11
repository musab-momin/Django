import React, { useEffect, useState } from "react";
import './App.css';
import Review from "./reviews/Review";
import data from './reviews/data'
import BasicForm from './forms/BasicForm'

// function App() {
//     const url = 'https://course-api.com/react-tours-project'

//     const [index, setIndex] = useState(0)
//     const [count, setCount] = useState(0)
//     const [tource, setTource] = useState([])
//     const [loading, setLoading] = useState(true)

//     // console.log('componenet gets render')

//     const validator = (num)=>{
//         let tmp = num
        
//         if (tmp === index)
//             tmp = num - 1

//         if (data.length === num)
//             tmp = 0

//         if(tmp < 0)
//             tmp = data.length - 1
        
//         return tmp   
//     }


//     const nextHandler = ()=>{
            
//         (data.length-1) !== index ? setIndex(index+1) : setIndex(0)

        
//     }

//     const prevHandler = ()=>{
//         if(index-1 < 0)
//             setIndex(data.length-1)
//         else
//             setIndex(index - 1)        
//     }

//     const surprice = ()=>{
//         let temp = Math.floor(Math.random() * data.length)
//         if (index === temp)
//             temp -=1
//         if(temp < 0)
//             temp = data.length-1

//         console.log(`This is temp ${temp} \n This is current index ${index}`)
//         setIndex(temp)
//     }

//     const fetchTours = async()=>{
//         // fetch(url).then((response)=>{
//         //     return response.json()
//         // }).then((data)=>{
//         //     console.log(data)
//         //     setTource(data)
//         //     setLoading(false)
//         // }).catch(err=>console.error(err))
//         try{
//             const response =  await fetch(url)
//             const data = await response.json()
//             setTource(data)
//             setLoading(false)

//         }catch(err){
//             console.error('got error while fetching resposne', err)
//             setLoading(false)
//         }
        
//     }

//     useEffect(()=>{
//         console.log('hello world..')
//         fetchTours() 
//     },[])

//     if(loading){
//         return (<p>Loading...</p>)
//     }

//     return (
//         <>
//             {/* <Review data={data}  index = {index} nextHandler = {nextHandler} prevHandler = { prevHandler } surprice = {surprice} />
//              */}
//              <div className="">
//                 <h2>Hello world...</h2>
//                 <button onClick={()=>{setIndex(index+1)}} >click me</button><br />
//                 <button onClick={()=>{setCount(count+1)}}> button </button>
//              </div>
//              <div>
//                 {
//                     tource.map(ele=><button key={ele.id} >{ele.id}</button>)
//                 }
//              </div>
//         </>
//     )
// }
// export default App;



function App() {
    return(
    <>
        <BasicForm />
    
    </>)
}


export default App;