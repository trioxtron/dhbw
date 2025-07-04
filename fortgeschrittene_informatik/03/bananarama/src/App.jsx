import React from 'react'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { useLocation } from 'react-router-dom';

import restaurantLogo from './assets/logo.png'
import kitchenImage from './assets/kitchen.jpg'

import './App.css'
import Home from './pages/Home'
import Imprint from './pages/Imprint'
import Contact from './pages/Contact'

import Header from './components/Header/Header'


function App() {
    let images = {
        restaurantLogo: restaurantLogo,
        kitchenImage: kitchenImage
    };

    return (
        <div className="app-container">
            <Header items={images}/>

            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/impressum" element={<Imprint />} />
                <Route path="/kontakt" element={<Contact />} />
            </Routes>


            <div className='footer'>
                <a href="/impressum">Impressum</a> | 
                <a href="/datenschutz"> Datenschutz</a> | 
                <a href="/kontakt"> Kontakt</a>
                <p>&copy; 2023 Bananarama. Alle Rechte vorbehalten.</p>
            </div>
        </div>
    )
}

export default App
