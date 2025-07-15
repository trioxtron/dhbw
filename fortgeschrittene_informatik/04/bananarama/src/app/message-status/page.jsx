'use client';
import { useSearchParams } from 'next/navigation';

export default function MessageStatusPage({ params }) {
    const searchParams = useSearchParams();
    const name = searchParams.get('name');
    const email = searchParams.get('email');
    const status = searchParams.get('status');

    console.log('Received parameters:', { name, email, status });


    return (
        <div className="content">
            <h1>Nachrichtenstatus</h1>
            {name && email && status ? (
                <div>
                    <p><strong>Name:</strong> {decodeURIComponent(name)}</p>
                    <p><strong>E-Mail:</strong> {decodeURIComponent(email)}</p>
                    <p><strong>Status:</strong> {decodeURIComponent(status)}</p>
                </div>
            ) : (
                <p>Keine Informationen verfügbar.</p>
            )}
        </div>
    );
}
