import React, { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/Form.css";
import LoadingIndicator from "./LoadingIndicator";

function Form({ route, method }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [role, setRole] = useState("");
    const [fname, setFname] = useState("");
    const [lname, setLname] = useState("");
    const [email_id, setEmailId] = useState("");
    const [password2, setPassword2] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();
    const name = method === "login" ? "Login" : "Register";

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        try {
            const data = { username, password, role, fname, lname, email_id, password2 };
            let res;
            if (method === "login") {
                // For login, post to the token endpoint
                res = await api.post("/api/user/auth/token", { username, password });
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
            } else {
                // For register, post to the register endpoint
                res = await api.post(route, data);
                // Redirect to login page after successful registration
                navigate("/login");
            }

            // If the response is successful, handle redirection based on role
            if (res.status === 200 && method === "login") {
                // Get user info after login to determine the role
                const userInfo = await api.get("/api/user/profile/");
                const role = userInfo.data.role;

                if (role === "Normal User") {
                    navigate("/dashboard"); 
                } else if (role === "Surgeon") {
                    navigate("/dashboard");
                } else if (role === "Teleradiologist") {
                    navigate("/dashboard");
                } else if (role === "Radiologist") {
                    navigate("/dashboard");
                } else {
                    // Handle other roles or unexpected scenarios
                    navigate("/");
                }
            }
        } catch (error) {
            alert(error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="form-container">
            <h1>{name}</h1>
            <input
                className="form-input"
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Username"
            />
            <input
                className="form-input"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
            />
            {method === "register" && (
                <div>
                    <input
                        className="form-input"
                        type="text"
                        value={email_id}
                        onChange={(e) => setEmailId(e.target.value)}
                        placeholder="Email"
                    />
                    <input
                        className="form-input"
                        type="password"
                        value={password2}
                        onChange={(e) => setPassword2(e.target.value)}
                        placeholder="Confirm Password"
                    />
                    <input
                        className="form-input"
                        type="text"
                        value={fname}
                        onChange={(e) => setFname(e.target.value)}
                        placeholder="First Name"
                    />
                    <input
                        className="form-input"
                        type="text"
                        value={lname}
                        onChange={(e) => setLname(e.target.value)}
                        placeholder="Last Name"
                    />
                    <select
                        className="form-input"
                        value={role}
                        onChange={(e) => setRole(e.target.value)}
                        placeholder="Role"
                    >
                        <option value="">Select a role</option>
                        <option value="Normal User">Normal User</option>
                        <option value="Surgeon">Surgeon</option>
                        <option value="Teleradiologist">Teleradiologist</option>
                        <option value="Radiologist">Radiologist</option>
                    </select>
                </div>
            )}
            {loading && <LoadingIndicator />}
            <button className="form-button" type="submit">
                {name}
            </button>
        </form>
    );
}

export default Form;
