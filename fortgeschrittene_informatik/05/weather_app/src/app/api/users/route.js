let users = [
    {
        id: 1,
        name: 'John Doe',
        email: 'john@john.de',
        location: 'Berlin',
    },
]

export async function POST(request) {
    const { name, email, location } = await request.json();

    console.log('Received data:', { name, email, location });

    // Validate input
    if (!name || !email ) {
        return new Response(JSON.stringify({ error: 'Name and Email fields are required' }), {
            status: 400,
            headers: { 'Content-Type': 'application/json' },
        });
    }

    // Check if user is already registered
    const existingUser = users.find(user => user.email === email);
    if (existingUser) {
        console.log('User already exists:', existingUser.id);
        const currentID = existingUser.id;
        console.log('Returning existing user ID:', currentID);
        return  new Response(JSON.stringify({ id: currentID }), {
            status: 200,
            headers: { 'Content-Type': 'application/json' },
        });
    }

    if (!location) {
        return new Response(JSON.stringify({ error: 'Location field is required to register new user' }), {
            status: 400,
            headers: { 'Content-Type': 'application/json' },
        });
    }

    // Simulate saving to a database
    const newUser = {
        id: Date.now(),
        name,
        email,
        location,
    }

    users.push(newUser);
    console.log('New user added:', newUser);

    return new Response(JSON.stringify({ id: newUser.id }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
    });
}

export async function GET(request) {
    const { searchParams } = new URL(request.url);
    const id = searchParams.get('id');

    console.log('Fetching user with ID:', id);

    // Find user by ID
    const user = users.find(user => user.id === parseInt(id));
    if (!user) {
        return new Response(JSON.stringify({ error: 'User not found' }), {
            status: 404,
            headers: { 'Content-Type': 'application/json' },
        });
    }

    console.log('User found:', user);
    return new Response(JSON.stringify(user.location), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
    });
}
