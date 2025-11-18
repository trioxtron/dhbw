import Link from 'next/link';

import LoginForm from '../components/Input/Form';

export default function Home() {
    return (
        <div>
            <h1>Register to be able to see your weather!</h1>
            <LoginForm isLogin={false} />
            <div className="login-choice">
                <Link href="/login">nvm... LOGIN</Link>
            </div>
        </div>
    );
}
