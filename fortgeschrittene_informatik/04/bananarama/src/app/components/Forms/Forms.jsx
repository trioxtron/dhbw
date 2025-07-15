// Make sure to use client-side rendering for this component
// Because of the use of hooks like useState
'use client';

import React, { useState } from 'react';
import InputField from './InputField/InputField';
import { useRouter } from 'next/navigation';

import { sendMessage } from '@/app/actions'; // Importieren Sie die getMessage-Funktion

const Forms = () => {
    const router = useRouter();

    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Hier können Sie die Logik zum Senden der Formulardaten hinzufügen
        console.log('Form submitted:', { name, email, message });

        sendMessage({ name, email, message })
            .then(data => {
                console.log('Message sent successfully:', data);
                router.push(`/received?name=${encodeURIComponent(data.name)}&id=${encodeURIComponent(data.id)}`);
            })
            .catch(error => {
                console.error('Error sending message:', error);
                // Hier können Sie eine Fehlermeldung anzeigen oder eine andere Aktion durchführen
            });
    }

    return  (
        <form onSubmit={handleSubmit}>
            <InputField
                label="Name"
                type="text"
                value={name}
                onChange={setName}
            />
            <InputField
                label="E-Mail"
                type="email"
                value={email}
                onChange={setEmail}
            />
            <div className="input-field">
                <label>
                    Nachricht
                    <textarea
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        rows="4"
                        required
                    ></textarea>
                </label>
            </div>
            <button className="submit-button" type="submit">Absenden</button>
        </form>
    );
};

export default Forms;
