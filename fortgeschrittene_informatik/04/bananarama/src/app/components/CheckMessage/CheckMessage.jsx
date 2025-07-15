// Make sure to use client-side rendering for this component
// Because of the use of hooks like useState
'use client';

import React, { useState } from 'react';
import InputField from './InputField/InputField';
import { useRouter } from 'next/navigation';
import { getMessage } from '@/app/actions'; 

const Forms = () => {
    const router = useRouter();

    const [messageID, setID] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();

        // Hier können Sie die Logik zum Abrufen der Nachricht hinzufügen
        console.log('Form submitted:', { messageID });
        getMessage({ id: messageID })
            .then(data => {
                console.log('Fetched message:', data);
                // Hier können Sie die Logik zum Weiterleiten oder Anzeigen der Nachricht hinzufügen
                router.push(`/message-status?name=${encodeURIComponent(data.name)}&email=${encodeURIComponent(data.email)}&status=${encodeURIComponent(data.status)}`);
            })
            .catch(error => {
                console.error('Error fetching message:', error);
            });
    }

    return  (
        <form onSubmit={handleSubmit}>
            <InputField
                label="Message ID"
                type="text"
                value={messageID}
                onChange={setID}
            />
            <button className="submit-button" type="submit">Absenden</button>
        </form>
    );
};

export default Forms;
