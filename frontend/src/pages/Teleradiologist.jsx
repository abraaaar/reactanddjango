import React, { useState, useEffect } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";

function Teleradiologist({ handleLogout }) {
    const [data, setData] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchData = async () => {
            const result = await api.get("/api/volume");
            setData(result.data);
        };

        fetchData();
    }, []);

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
            <h1>Welcome, Teleradiologist!</h1>
            <table>
                <thead>
                    <tr>
                        <th>Username</th>
                        <th>Uploaded images</th>
                        <th>Organization name</th>
                        <th>Mark Status</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map(item => (
                        item.status === 'UPLOADED' && (
                            <tr key={item.record_id}>
                                <td>{item.uploaded_by.username}</td>
                                <td>{item.volume_meta}</td>
                                <td>{item.org.org_name}</td>
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

export default Teleradiologist;
