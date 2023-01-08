import React from "react"

export default function Card({imageUrl, location, googleMapsUrl, title, startDate, endDate, description}) {
    return (
        <div className="card--container">
            <img className="card--image" src={imageUrl} />
            <div className="card--info-container">
                <div className="card--info--location-container">
                    <p className="card--info--location-icon icon"></p>
                    <p className="card--info--location-title">{location.toUpperCase()}</p>
                    <a className="card--info--location-google-maps-url" href={googleMapsUrl} target="_blank">View on Google Maps</a>
                </div>
                <h1 className="card--info-title">{title}</h1>
                <p className="card--info-date">{startDate} - {endDate}</p>
                <p className="card--info-description">{description}</p>
            </div>
        </div>
    )
}
