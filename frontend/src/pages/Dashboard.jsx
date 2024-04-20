import React, { useState, useEffect } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";

function Dashboard() {
    const [data, setData] = useState([]);
    const [role, setRole] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        const fetchData = async () => {
            const result = await api.get("/api/user/profile");
            setRole(result.data.role);
            const volumeResult = await api.get("/api/volume");
            setData(volumeResult.data);
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

    if (role === "Normal User") {
        return (
            <div>
                <h1>Welcome, Normal User!</h1>
                <input type="file" name="file" onChange={changeHandler} />
                {isFilePicked ? (
                    <div>
                        <p>Filename: {selectedFile.name}</p>
                        <p>Filetype: {selectedFile.type}</p>
                        <p>Size in bytes: {selectedFile.size}</p>
                        <p>
                            lastModifiedDate:{' '}
                            {selectedFile.lastModifiedDate.toLocaleDateString()}
                        </p>
                    </div>
                ) : (
                    <p>Select a file to show details</p>
                )}
                <button onClick={handleSubmission}>Submit</button>
                <button onClick={handleLogout}>Logout</button>
            </div>
        );
    } else if (role === "Radiologist") {
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
    } else if (role === "Teleradiologist") {
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
    } else if (role === "Surgeon") {
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
}

export default Dashboard;
