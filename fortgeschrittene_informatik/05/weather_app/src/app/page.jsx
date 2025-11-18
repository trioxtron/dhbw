import Link from 'next/link';

export default function Home() {
    return (
        <div>
            <h1> Welcome to your weather app!</h1>
            <div className="login-choice">
                <Link href="/login">LOGIN</Link>
                <Link href="/register">REGISTER</Link>
            </div>
        </div>
    );
}
