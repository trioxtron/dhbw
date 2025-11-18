'use server';

export async function sendUser({ name, email, location }) {
    console.log('Sending user:', { name, email, location });
    const response = await fetch('http://localhost:3000/api/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: name, email: email, location: location }),
    });
    if (!response.ok) {
        throw new Error('Failed to send user');
    }
    const data = await response.json();
    return data;
}

export async function receiveWeather({ id }) {
    if (!id) {
        throw new Error('User ID is required to fetch weather');
    }

    const weather_response = await fetch(`http://localhost:3000/api/weather?id=${encodeURIComponent(id)}`, {
        method: 'GET'
    });

    if (!weather_response.ok) {
        throw new Error('Failed to fetch weather data');
    }
    const weatherData = await weather_response.json();
    console.log('Weather data fetched:', weatherData);
    return weatherData;
}

