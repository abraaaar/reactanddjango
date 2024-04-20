import React, { useState, useEffect } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";

function Surgeon() {
    const [data, setData] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchData = async () => {
            const result = await api.get("/api/volume");
            setData(result.data);
        };

        fetchData();
    }, []);

    const handleLogout = () => {
        localStorage.removeItem('ACCESS_TOKEN');
        localStorage.removeItem('REFRESH_TOKEN');
        navigate('/login');
    };

    return (
        <div>
            <h1>Welcome, Surgeon!</h1>
            <table>
                <thead>
                    <tr>
                        <th>Username</th>
                        <th>Uploaded images</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map(item => (
                        item.status === 'COMPLETED' && (
                            <tr key={item.record_id}>
                                <td>{item.uploaded_by.username}</td>
                                <td>{item.volume_meta}</td>
                            </tr>
                        )
                    ))}
                </tbody>
            </table>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default Surgeon;
