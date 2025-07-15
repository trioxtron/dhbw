let messages = [
    {
        id: 1,
        name: 'John Doe',
        email: 'john@john.de',
        message: 'Hello, this is a test message.',
        status: 'unread',
    },
]

export async function POST(request) {
    const { name, email, message } = await request.json();

    console.log('Received data:', { name, email, message });

    // Validate input
    if (!name || !email || !message) {
        return new Response(JSON.stringify({ error: 'All fields are required' }), {
            status: 400,
            headers: { 'Content-Type': 'application/json' },
        });
    }

    // Simulate saving to a database
    const savedMessage = {
        id: Date.now(),
        name,
        email,
        message,
        status: 'unread',
    };

    messages.push(savedMessage);
    console.log('Saved message:', savedMessage);
    console.log(messages);

    // Return the saved message
    return new Response(JSON.stringify(savedMessage), {
        status: 201,
        headers: { 'Content-Type': 'application/json' },
    });
}


export async function GET(request) {
    const { searchParams } = new URL(request.url);
    const id = searchParams.get('id');

    console.log('Received ID: ', id);
    // get the type of id
    if (id) {
        console.log('ID type: ', typeof id);
    }

    if (!id) {
        return new Response(JSON.stringify({ error: 'ID parameter is missing' }), {
            status: 400,
            headers: { 'Content-Type': 'application/json' },
        });
    }

    if (messages.length === 0) {
        return new Response(JSON.stringify({ error: 'No messages found' }), {
            status: 404,
            headers: { 'Content-Type': 'application/json' },
        });
    }

    // Find the message by ID
    const curr_message = messages.find(message => message.id === parseInt(id, 10));
    console.log('Current message: ', curr_message);

    if (!curr_message) {
        return new Response(JSON.stringify({ error: 'Message not found' }), {
            status: 404,
            headers: { 'Content-Type': 'application/json' },
        });
    }

    return new Response(JSON.stringify(curr_message), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
    });
}
