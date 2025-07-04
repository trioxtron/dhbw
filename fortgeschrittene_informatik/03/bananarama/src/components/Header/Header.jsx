import React from 'react';
import './Header.css';

import { useLocation } from 'react-router-dom';
import { Link } from 'react-router-dom';

const Header = ({ items }) => {
    const location = useLocation();
    const isHomePage = location.pathname === "/";

    return (
        <div className={`header ${isHomePage ? 'header-home' : 'header-compact'}`}>
            <div className="header-bar">
                <Link to="/" className="logo-link">
                    <img src={items.restaurantLogo} alt="Restaurant Logo" className="logo" />
                </Link>
                <nav>
                    <ul>
                        <li><a href="#food">Speisen</a></li>
                        <li><a href="#drinks">Getränke</a></li>
                    </ul>
                </nav>
            </div>

            {isHomePage && (
                <div className="title-image-box">
                    <div className="title-text-box">
                        <h1 className="title">BANANARAMA</h1>
                        <p>Musterstraße 3, 12345 Musterstadt</p>
                    </div>
                    <img src={items.kitchenImage} alt="Restaurant Kitchen" className="frontimage" />
                </div>
            )}
        </div>
    );
};

export default Header;
