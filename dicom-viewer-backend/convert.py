import numpy as np
import os
import sys
import traceback
from PIL import Image
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
    traceback.print_exc()
    sys.exit(1)

# 🔍 **Step 1: Check if the DICOM file is a PDF**
if dcm.SOPClassUID == "1.2.840.10008.5.1.4.1.1.104.1" and hasattr(dcm, "EncapsulatedDocument"):
    try:
        pdf_path = os.path.join(output_folder, os.path.basename(dicom_file) + ".pdf")
        with open(pdf_path, "wb") as f:
            f.write(dcm.EncapsulatedDocument)

        print(f"✅ Extracted PDF saved to: {pdf_path}")
        print(os.path.basename(pdf_path))  # Return filename for backend
        sys.exit(0)  # Exit since we are not processing an image
    except Exception as e:
        print("❌ Error processing DICOM PDF:")
        traceback.print_exc()
        sys.exit(1)

# 🔍 **Step 2: Process the DICOM file as an image**
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
