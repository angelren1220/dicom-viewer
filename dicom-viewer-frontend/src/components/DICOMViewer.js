import React, { useState } from "react";
import axios from "axios";

const DICOMViewer = () => {
    const [images, setImages] = useState([]);
    const [file, setFile] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const uploadFile = async () => {
      if (!file) {
          alert("Please select a file first.");
          return;
      }
  
      const formData = new FormData();
      formData.append("dicomdir", file);
  
      try {
          const response = await axios.post("http://localhost:5001/upload", formData, {
              headers: { "Content-Type": "multipart/form-data" },
          });
  
          console.log("🔍 Backend Response:", response.data);  // Log response
  
          if (Array.isArray(response.data)) {
              setImages(response.data);  // ✅ Only set state if it's an array
          } else if (typeof response.data === "object" && response.data.images) {
              setImages(response.data.images);  // ✅ Handle if backend returns { images: [...] }
          } else {
              console.error("❌ Unexpected response format:", response.data);
          }
      } catch (error) {
          console.error("❌ Error uploading file:", error);
      }
  };
  

    return (
        <div>
            <h1>DICOM Viewer</h1>
            <input type="file" onChange={handleFileChange} />
            <button onClick={uploadFile}>Upload</button>

            <div className="gallery">
                {images.map((img, index) => (
                    <img key={index} src={`http://localhost:5001/images/${img}`} alt="DICOM" className="dicom-image" />
                ))}
            </div>
        </div>
    );
};

export default DICOMViewer;
