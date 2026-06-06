from PIL import Image
import os

input_folder = r"C:\Users\varun kumar\Desktop\Jarvis\www\images"
output_folder = os.path.join(input_folder, "compressed_500kb")

os.makedirs(output_folder, exist_ok=True)

max_size = 500 * 1024  

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        filepath = os.path.join(input_folder, filename)
        img = Image.open(filepath)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, base_name + ".jpg")

        quality = 85

        while True:
            img.save(output_path, "JPEG", optimize=True, quality=quality)
            if os.path.getsize(output_path) <= max_size or quality <= 20:
                break
            quality -= 5

        print(f"Compressed: {filename} -> {os.path.getsize(output_path)//1024} KB")

print("\n✅folder: " + output_folder)
