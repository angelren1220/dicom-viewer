# 📌 DICOM Viewer
A web-based DICOM file viewer that allows users to upload, view, and convert DICOM images to PNG format. The application provides a simple interface for medical imaging professionals to process and visualize medical scans, ensuring compatibility with various DICOM formats and compressed images.

## 🚀 Features
- Upload DICOM files
- Convert DICOM images to PNG
- View converted images in the browser

## 📂 Project Structure
```
📁 dicom-viewer
 ├── 📁 dicom-viewer-backend  # Backend (Node.js & Python)
 │   ├── server.js            # Express server
 │   ├── convert.py           # Python script for DICOM to PNG conversion
 │   ├── uploads/             # DICOM upload directory (ignored in Git)
 │   ├── converted/           # Converted images directory (ignored in Git)
 │   ├── .env                 # Environment variables (ignored in Git)
 │
 ├── 📁 dicom-viewer-frontend  # Frontend (React.js)
 │   ├── src/                 # React components
 │   ├── public/              # Public assets
 │   ├── package.json         # Frontend dependencies
 │
 ├── .gitignore               # Ignored files
 ├── README.md                # Project documentation
```

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/dicom-viewer.git
cd dicom-viewer
```

### **2️⃣ Backend Setup (Node.js + Python)**
#### **Install Dependencies**
```bash
cd dicom-viewer-backend
npm install  # Install Node.js dependencies
pip install -r requirements.txt  # Install Python dependencies
```
#### **Set Up Environment Variables**
Create a `.env` file inside `dicom-viewer-backend/` and add:
```ini
PYTHON_PATH=/Users/your-username/.pyenv/shims/python3
```

#### **Run the Backend**
```bash
node server.js
```

### **3️⃣ Frontend Setup (React.js)**
#### **Install Dependencies**
```bash
cd dicom-viewer-frontend
npm install
```
#### **Run the Frontend**
```bash
npm start
```
The app will be available at **`http://localhost:3000/`**.

## 🚀 Usage
1. Upload a DICOM file
2. The backend processes it and converts it to PNG
3. The converted image is displayed in the frontend

## 🚀 Tech Stack
### **Frontend:**
- **React.js** – For building the user interface
- **Axios** – To handle HTTP requests to the backend
- **Tailwind CSS** – For styling components

### **Backend:**
- **Node.js & Express.js** – To handle API requests
- **Python** – For DICOM image processing
- **Pydicom** – To read and process DICOM files
- **Pillow (PIL)** – To convert images to PNG format
- **GDCM & pylibjpeg** – For handling compressed DICOM images

### **Infrastructure & Deployment:**
- **Git & GitHub** – Version control and repository management
- **Dotenv** – For managing environment variables

## 📜 License
This project is open-source and available under the MIT License.

