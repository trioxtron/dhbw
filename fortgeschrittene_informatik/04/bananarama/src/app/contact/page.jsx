import React from 'react';
import Forms from '../components/Forms/Forms';

import Link from 'next/link';

function Contact() {
    return (
        <div className="content">
            <h1>Kontakt</h1>
            <p> Bei Fragen oder Anregungen können Sie uns gerne kontaktieren: </p>
            <Forms />
            <Link href="/check-message" className="check-message">Checken Sie Ihre Message!</Link>
        </div>
    );
}

export default Contact;

