// Make sure to use client-side rendering for this component
// Because of the use of hooks like useState
'use client';

import React, { useState } from 'react';
import InputField from './InputField/InputField';
import { useRouter } from 'next/navigation'; 

import { sendUser } from '@/app/actions'; 


const Forms = ({ isLogin }) => {
    const router = useRouter();

    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [location, setLocation] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Hier können Sie die Logik zum Senden der Formulardaten hinzufügen
        console.log('Form submitted:', { name, email, location });

        sendUser({ name, email, location })
        .then((data) => {
            console.log('User sent successfully:', data);
            // Hier können Sie nach dem erfolgreichen Senden der Daten weitere Aktionen durchführen
            if (isLogin) {
                // Logik für Login
                console.log('Login successful for user:', name);
            } else {
                // Logik für Registrierung
                console.log('Registration successful for user:', name);
            }

            router.push(`/weather/${encodeURIComponent(data.id)}`);
        })
        .catch((error) => {
            console.error('Error sending user:', error);
        })

    }

    return (
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
            {isLogin ? (
                <div>
                    <button className="submit-button" type="submit">Login</button>
                </div>
            ) : (
                <div>
                    <InputField
                        label="Standort"
                        type="text"
                        value={location}
                        onChange={setLocation}
                    />
                    <button className="submit-button" type="submit">Register</button>
                </div>
            )}
        </form>
    );
};

export default Forms;

