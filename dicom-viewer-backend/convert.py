import numpy as np
import os
import sys
import traceback
from PIL import Image

import sys
import os

# Find and add GDCM's Python bindings to the path
gdcm_path = "/opt/homebrew/Cellar/gdcm/3.0.24/lib/python3.9/site-packages"
if os.path.exists(gdcm_path):
    sys.path.append(gdcm_path)
else:
    print("❌ GDCM path not found:", gdcm_path)

import pydicom
from pydicom import config
import pydicom.pixel_data_handlers.gdcm_handler
import pydicom.pixel_data_handlers.pylibjpeg_handler

# Manually enable handlers
config.use_handlers = [
    pydicom.pixel_data_handlers.pylibjpeg_handler,
    pydicom.pixel_data_handlers.gdcm_handler,
    pydicom.pixel_data_handlers.pillow_handler
]

print("✅ GDCM Path Added to Python:", gdcm_path)



# Get the uploaded file
dicom_file = sys.argv[1]
output_folder = "converted"
os.makedirs(output_folder, exist_ok=True)

# Read the DICOM file
try:
    dcm = pydicom.dcmread(dicom_file, force=True)
    print(f"✅ Successfully read DICOM file: {dicom_file}")
except Exception as e:
    print("❌ Error reading DICOM file:")
    traceback.print_exc()  # Prints full error details
    sys.exit(1)

# Check if the DICOM contains image data (PixelData)
if not hasattr(dcm, "PixelData"):
    print("❌ Error: No PixelData found in this DICOM file. It may not be an image.")
    sys.exit(1)

# Convert image to PNG
try:
    pixel_array = dcm.pixel_array

    # Normalize pixel data for PNG conversion
    pixel_array = ((pixel_array - pixel_array.min()) /
                   (pixel_array.max() - pixel_array.min()) * 255).astype(np.uint8)

    # Save as PNG
    img = Image.fromarray(pixel_array)
    img_path = os.path.join(output_folder, os.path.basename(dicom_file) + ".png")
    img.save(img_path, "PNG")

    print(f"✅ Converted DICOM to PNG: {img_path}")
    print(os.path.basename(img_path))  # Return image filename for backend

except Exception as e:
    print("❌ Error processing DICOM image:")
    traceback.print_exc()
    sys.exit(1)
