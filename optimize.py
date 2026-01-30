import os
import glob
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from PIL import Image
except ImportError:
    print("Pillow not found, installing...")
    install('Pillow')
    from PIL import Image

def optimize_images():
    print("Starting image optimization...")
    files = glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.png")
    # Filter specific files
    files = [f for f in files if "wechat" not in f and "hero" not in f and "optimized" not in f]

    for i, file_path in enumerate(files):
        try:
            with Image.open(file_path) as img:
                max_width = 1000
                if img.width > max_width:
                    ratio = max_width / img.width
                    new_height = int(img.height * ratio)
                    img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                
                output_filename = f"gallery_img_{i+1}.webp"
                img.save(output_filename, "WEBP", quality=80)
                print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Failed {file_path}: {e}")

if __name__ == "__main__":
    optimize_images()
