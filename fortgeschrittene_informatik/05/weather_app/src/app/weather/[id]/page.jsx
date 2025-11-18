import { receiveWeather } from '@/app/actions';

import Weather from '../../components/Weather/Weather';

export default async function Home({ params }) {
    const { id } = await params;
    console.log('[WEATHER SITE] Fetching weather for user ID:', id);
    let weather = await receiveWeather({ id: id })

    const location = weather.location

    console.log('[WEATHER SITE] Your location', weather.location);

    return (
        <div className='content'>
            <h1>Your weather in {location}</h1>
            <div className='weather-container'>
                {weather.forecast.slice(1).map((forecastItem, i) => (
                    <Weather
                    key={i}
                    date={forecastItem.date}
                    max={forecastItem.day.maxtemp_c}
                    min={forecastItem.day.mintemp_c}
                    condition={forecastItem.day.condition.text}
                    />
                ))}
            </div>
        </div>
    );
}
