export async function GET(request) {
    const { searchParams } = new URL(request.url);
    const id = searchParams.get('id');

    console.log('Getting location of user ID:', id);
    const users_response = await fetch(`http://localhost:3000/api/users/?id=${encodeURIComponent(id)}`, {
        method: 'GET'
    });

    if (!users_response.ok) {
        throw new Error('Failed to fetch user location');
    }

    const data = await users_response.json();
    console.log('User location fetched', data);
    const location = data;
    console.log('Fetching weather for location:', location);


    const weather_response = await fetch(`http://api.weatherapi.com/v1/forecast.json?key=31aa236a35ba4e0688a234457240606&q=${encodeURIComponent(location)}&days=12&aqi=no&alerts=no`, {
        method: 'GET'
    });
    if (!weather_response.ok) {
        throw new Error('Failed to fetch weather data');
    }
    const weatherData = await weather_response.json();

    // Return forecast and location
    return new Response(JSON.stringify({ forecast: weatherData.forecast.forecastday, location: location }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
    });
}
