import React, { useState, useEffect } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import NormalUser from "./NormalUser";
import Radiologist from "./Radiologist";
import Teleradiologist from "./Teleradiologist";
import Surgeon from "./Surgeon";

function Dashboard() {
    const [role, setRole] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        const fetchData = async () => {
            const result = await api.get("/api/user/profile?membership=true");
            setRole(result.data.role);
        };

        fetchData();
    }, []);

    const handleLogout = () => {
        localStorage.removeItem('ACCESS_TOKEN');
        localStorage.removeItem('REFRESH_TOKEN');
        navigate('/login');
    };

    if (role === "Normal User") {
        return <NormalUser handleLogout={handleLogout} />;
    } else if (role === "Radiologist") {
        return <Radiologist handleLogout={handleLogout} />;
    } else if (role === "Teleradiologist") {
        return <Teleradiologist handleLogout={handleLogout} />;
    } else if (role === "Surgeon") {
        return <Surgeon handleLogout={handleLogout} />;
    } else {
        return <div>Loading...</div>;
    }
}

export default Dashboard;
