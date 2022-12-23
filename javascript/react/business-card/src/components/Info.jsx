import React from "react"

export default function Info() {
    return (
        <div className="info--container"> 
            <img src="/src/images/geert.jpeg" className="info--pfp" />
            <h1 className="info--name">Geert</h1>
            <h3 className="info--role">Frontend developer</h3>
            <p className="info--website">geert.com</p>
            <div className="info--button-container">
                <button className="info--email-button"> Email</button>
                <button className="info--linkedin-button"> LinkedIn</button>  
            </div>
        </div>
    )
}
