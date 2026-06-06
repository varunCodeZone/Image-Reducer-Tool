# Image Compression Utility Tool 🖼️

A lightweight, efficient Python-based automation tool designed to optimize image storage by batch-compressing large image files while maintaining visual quality.

## 🚀 Features
- **Batch Processing**: Automatically scans a folder and processes multiple images (PNG, JPG, JPEG, WEBP).
- **Adaptive Compression**: Uses an iterative algorithm to reduce file size while targeting a specific limit (e.g., 500KB).
- **Format Conversion**: Automatically converts various image formats to standard JPEG for consistency.
- **Safety**: Creates a separate folder for output files to prevent data loss.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Library**: Pillow (PIL)
- **Utilities**: OS Module for file system interaction

## 📋 How to Use
1. **Install Dependencies**:
   ```bash
   pip install Pillow
   ```
   
2. **Configure Paths: Update the input_folder path in the script to point to your image directory.**

1. **Run the Script:**:
   ```bash
   python script_name.py
   ```


## 💡 Why I built this
```bash
As a developer, I often deal with large image assets that slow down web performance. This tool was built to automate the tedious task of manual resizing, allowing for faster workflow and optimized web-ready assets.
```

**Created by VARUN KUMAR**