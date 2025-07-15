//import styles from "./page.module.css";
import Menu from './components/Menu/Menu';


export default function Home() {
    const food = [
        {name: "Pasta", price: 12, image: "/food/pasta.jpg"},
        {name: "Lamm", price: 18, image: "/food/lamb.jpg"},
        {name: "Rindersteak", price: 22, image: "/food/meat.jpg"},
        {name: "Lachsfilet", price: 16, image: "/food/salmon.webp"}
    ]
    const drinks = [
        {name: "Mojito", price: 7, image: "/drinks/drink1.webp"},
        {name: "Caipirinha", price: 8, image: "/drinks/drink2.avif"},
        {name: "Piña Colada", price: 8, image: "/drinks/drink3.jpg"},
        {name: "Tequila Sunrise", price: 6, image: "/drinks/drink4.jpg"}
    ]
    return (
        <div className="app-container">

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
        </div>
    );
}
