import React from 'react';
import Link from "next/link";


const Footer = () => {
    return (
        <div className='footer'>
            <Link href="/imprint">Impressum</Link> |
            <Link href="/contact"> Kontakt</Link>
            <p>&copy; 2023 Bananarama. Alle Rechte vorbehalten.</p>
        </div>
    );
}

export default Footer;
