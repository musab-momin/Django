import React from "react"
import {Link} from 'react-router-dom'

const Header = ()=>{
    return(
        <header>
        <div className="container">
            <Link to='/' style={{ textDecoration: 'none' }}>
                <h2 className="logo"> PersonalSpace </h2>
            </Link>
        </div>
    </header>
    )
}

export default Header