'use client';
import { useSearchParams } from 'next/navigation';

import Link from 'next/link';

export default function Received () {
    const searchParams = useSearchParams();
    const name = searchParams.get('name');
    const id = searchParams.get('id');

    return (
        <div className="content">
            <h1>Vielen Dank, {decodeURIComponent(name)}!</h1>
            <p>Ihre Nachricht wurde erfolgreich gesendet.</p>
            <p>Ihre Message ID lautet: <strong>{decodeURIComponent(id)}</strong></p>
            <Link className="check-message" href="/check-message">Checken Sie Ihre Message!</Link>
        </div>
    );
}
