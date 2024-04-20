import Form from "../components/Form"

function Login() {
    return <Form route="/api/user/auth/token" method="login" />
}

export default Login
