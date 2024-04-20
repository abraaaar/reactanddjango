import React, { useState, useEffect } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";

function Radiologist() {
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

    const handleMarkAsComplete = async (record_id) => {
        try {
            await api.put(`/api/volume/${record_id}`, { status: 'COMPLETED' });
            setData(data.map(item => item.record_id === record_id ? { ...item, status: 'COMPLETED' } : item));
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <h1>Welcome, Radiologist!</h1>
            <table>
                <thead>
                    <tr>
                        <th>Username</th>
                        <th>Uploaded images</th>
                        <th>Mark Status</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map(item => (
                        item.status === 'UPLOADED' && (
                            <tr key={item.record_id}>
                                <td>{item.uploaded_by.username}</td>
                                <td>{item.volume_meta}</td>
                                <td><button onClick={() => handleMarkAsComplete(item.record_id)}>Mark as Complete</button></td>
                            </tr>
                        )
                    ))}
                </tbody>
            </table>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default Radiologist;
