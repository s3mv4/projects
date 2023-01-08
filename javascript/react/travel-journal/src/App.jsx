import { useState } from 'react'
import Navbar from "./components/Navbar"
import Card from "./components/Card"
import data from "./data"

function App() {
    const cards = data.map(item => {
        return (
            <Card 
                key={item.id}
                {...item}
            />
        )
    })
    return (
        <div className="container"> 
            <Navbar />
            <div className="cards--container">
                {cards}
            </div>
        </div>
    )
}

export default App
