import React, { useEffect, useState } from "react";
import {Link} from 'react-router-dom'
import Header from './Header'

const Records = () => {

    const [loading, setLoading] = useState(true)
    const [records, setRecords] = useState([])

    const fetchRecords = async ()=>{
        setLoading(true)
        try{
            const response = await fetch('http://localhost:8000/api/')
            const records = await response.json()
            setRecords(records)
            console.log(records);
            setLoading(false)
        }catch(err){
            console.warn(err)
            setLoading(false)
        }
    }

    useEffect(()=>{
        fetchRecords()
    }, [])

    if(loading){
        return(
            <main className='container mr-4'>
                <h2>Loading...</h2>
            </main>
        )
    }

    return (
        <>
        <Header />
        <main className='container mr-4'>
            <p>
                <Link to='/add'>
                Add new note...
                </Link> 
            </p>

            <section className="wrapper">
                {
                    records.map(ele=>{
                        return(
                            <div className="content" key={ele.id}>
                            <div className="content_heading">
                                <p>
                                    <Link to={`/read/${ ele.id }`} className='create-at'>
                                        {ele.created_at} 
                                    </Link>
                                </p>
                            </div>
                            <div className="content__body">
                                <p>
                                    {ele.content}
                                </p>
                            </div>
                        </div>
                        )
                    })
                }
               
            </section>

        </main>
        </>
    )
}

export default Records;
