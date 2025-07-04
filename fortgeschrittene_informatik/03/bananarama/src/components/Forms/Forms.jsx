import React, { useState } from 'react';
import InputField from './InputField/InputField';

const Forms = () => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');
    const [submitted, setSubmitted] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();
        // Hier können Sie die Logik zum Senden der Formulardaten hinzufügen
        console.log('Form submitted:', { name, email, message });
        console.log("SUBMITTED");
        setSubmitted(true);
    }

    let form = (
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

    if (submitted) {
        form = (
            <div className="thank-you-message">
                <h1><br/>Vielen Dank für Ihre Nachricht!</h1>
                <p>Wir werden uns so schnell wie möglich bei Ihnen melden.</p>
            </div>
        );
    }
    return (
        <>
            {form}
        </>
    );
};

export default Forms;
