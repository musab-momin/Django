import React from "react";



const Review = ({ data, index, nextHandler, prevHandler, surprice })=>{

    // console.log(index)

    return(<>
        <main className="container">
            <div>
                <h2>Our Reviews</h2>
            </div>
            <div className="card">
                <div className="card__head">
                    <img src={data[index].image} alt="#" className="img"/>
                </div>
                <div className="card__body">
                    <h4>{ data[index].name }</h4>
                    <p> { data[index].job } </p>
                    <p> { data[index].text } </p>
                </div>
                <div className="card__footer">
                    <button className="btn" onClick={()=>{ prevHandler() }}>prev</button>
                    <button className="btn" onClick={()=>{ nextHandler() }}>next</button>
                </div>
                <div>
                    <button className="btn" onClick={()=>{ surprice() }}>Surprise me</button>
                </div>
            </div>
        </main>

    </>)
}


export default Review;