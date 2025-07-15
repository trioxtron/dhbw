'use client';
import React from 'react';
import './Header.css';
import Link from 'next/link';

import { usePathname } from 'next/navigation';

const Header = () => {
    const location = usePathname();
    const isHomePage = location === "/";

    return (
        <div className={`header ${isHomePage ? 'header-home' : 'header-compact'}`}>
            <div className="header-bar">
                <Link href="/" className="logo-link">
                    <img src="/logo.png" alt="Restaurant Logo" className="logo" />
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
                    <img src="/kitchen.jpg" alt="Restaurant Kitchen" className="frontimage" />
                </div>
            )}
        </div>
    );
};

export default Header;
