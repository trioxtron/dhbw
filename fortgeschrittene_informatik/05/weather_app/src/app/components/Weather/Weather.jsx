// Make sure to use client-side rendering for this component
// Because of the use of hooks like useState
'use client';

import React from 'react';

const Weather = ({ date, max, min, condition }) => {
    return (
        <div className="weather-card">
            <h2>{date}</h2>
            <p className='weather-condition'>{condition}</p>
            <div className='weather-details'>
                <p>H: {max}°C</p>
                <p>L: {min}°C</p>
            </div>
        </div>
    );
};

export default Weather;

