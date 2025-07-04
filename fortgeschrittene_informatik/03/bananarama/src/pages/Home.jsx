import Menu from '../components/Menu/Menu';
import restaurantLogo from '../assets/logo.png';
import kitchenImage from '../assets/kitchen.jpg';

import pastaImg from '../assets/food/pasta.jpg';
import lambImg from '../assets/food/lamb.jpg';
import meatImg from '../assets/food/meat.jpg';
import salmonImg from '../assets/food/salmon.webp';

import drink1Img from '../assets/drinks/drink1.webp';
import drink2Img from '../assets/drinks/drink2.avif';
import drink3Img from '../assets/drinks/drink3.jpg';
import drink4Img from '../assets/drinks/drink4.jpg';


function Home() {
    const food = [
        { name: "Pasta", price: 12, image: pastaImg },
        { name: "Lamm", price: 18, image: lambImg },
        { name: "Rindersteak", price: 22, image: meatImg },
        { name: "Lachsfilet", price: 16, image: salmonImg }
    ];

    const drinks = [
        { name: "Mojito", price: 7, image: drink1Img },
        { name: "Caipirinha", price: 8, image: drink2Img },
        { name: "Piña Colada", price: 8, image: drink3Img },
        { name: "Tequila Sunrise", price: 6, image: drink4Img }
    ];

    return (
        <div className="content">
            <div className="info">
                <h2>Öffnungszeiten</h2>
                <p id="opening-hours">
                    Montag bis Freitag: 11:00 - 22:00 Uhr<br />
                    Samstag: 12:00 - 23:00 Uhr<br />
                    Sonntag: Geschlossen
                </p>
            </div>
            <div className="menu">
                <Menu heading="Speisen" items={food} />
                <Menu heading="Getränke" items={drinks} />
            </div>
        </div>
    );
}

export default Home;

