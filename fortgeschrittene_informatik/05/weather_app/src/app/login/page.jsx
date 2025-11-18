import Link from 'next/link';

import LoginForm from '../components/Input/Form';

export default function Home() {
    return (
        <div>
            <h1>Login to be able to see your weather!</h1>
            <LoginForm isLogin={true} />
            <div className="login-choice">
                <Link href="/register">nvm... REGISTER</Link>
            </div>
        </div>
    );
}
