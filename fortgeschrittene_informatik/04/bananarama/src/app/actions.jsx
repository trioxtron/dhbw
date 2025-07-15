'use server';

export async function sendMessage({ name, email, message }) {
    console.log('Sending message:', { name, email, message });
    const response = await fetch('http://localhost:3000/api/messages', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: name, email: email, message: message }),
    });
    if (!response.ok) {
        throw new Error('Failed to send message');
    }
    const data = await response.json();
    return data;
}

export async function getMessage({ id }) {
    const response = await fetch(`http://localhost:3000/api/messages/?id=${encodeURIComponent(id)}`, {
        method: 'GET',
//      headers: {
//          'Content-Type': 'application/json',
//      },
    });

    if (!response.ok) {
        throw Error('Failed to fetch message');
    }
    const data = await response.json();
    return data;
}
