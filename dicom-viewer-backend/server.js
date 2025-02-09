require("dotenv").config();
const PYTHON_PATH = process.env.PYTHON_PATH || "/usr/bin/python3";

const express = require("express");
const cors = require("cors");
const multer = require("multer");
const { exec } = require("child_process");
const fs = require("fs-extra");
const path = require("path");

const app = express();
app.use(cors());
app.use(express.json());

const storage = multer.diskStorage({
  destination: "uploads/",
  filename: (req, file, cb) => {
    cb(null, file.originalname); // Keep the original filename
  },
});
const upload = multer({ storage: storage });


app.post("/upload", upload.single("dicomdir"), (req, res) => {
  const dicomdirPath = req.file.path;

  // Convert DICOM to PNG using Python
  exec(`${PYTHON_PATH} convert.py ${dicomdirPath}`, (error, stdout, stderr) => {
    console.log("🔍 Python Script Output:\n", stdout);
    console.error("🚨 Python Script Errors:\n", stderr);

    if (error) {
      return res.status(500).json({ error: `Conversion failed: ${stderr}` });
    }

    const images = stdout.trim().split("\n").filter(img => img.endsWith(".png"));

    console.log("✅ Sending Images Array:", images);
    res.json(images);  // ✅ Ensure response is an array

  });
});

// Serve converted images
app.use("/images", express.static("converted"));

const PORT = process.env.PORT || 5001;

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
