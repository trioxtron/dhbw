import React from 'react';
import './Menu.css'

const menu = ({ heading, items}) => {
    return (
        <div className="menu">
            <div>
                <h1 id="food">{heading}</h1>
                <ul className="menu-category">
                    {items.map((item, index) => (
                        <li key={index}>
                            <img src={item.image} alt={item.name} className="menu-image" />
                            <p> {item.name} – <span className="price">{item.price},-</span> </p>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}
export default menu;
