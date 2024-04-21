import React, { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";

function NormalUser({ handleLogout }) {
    const [selectedFile, setSelectedFile] = useState();
    const [isFilePicked, setIsFilePicked] = useState(false);
    const [uploadedImage, setUploadedImage] = useState(null);
    const navigate = useNavigate();

    const changeHandler = (event) => {
        setSelectedFile(event.target.files[0]);
        setIsFilePicked(true);
    };

    const handleSubmission = async () => {
        const formData = new FormData();

        formData.append('File', selectedFile);

        try {
            const res = await api.post('/api/volume', formData);
            console.log(res);
            setUploadedImage(URL.createObjectURL(selectedFile));
        } catch (error) {
            console.error(error);
        }
    };

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
            {uploadedImage && <img src={uploadedImage} alt="Uploaded" />}
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default NormalUser;
