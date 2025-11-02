'''

MIT License

Copyright (c) 2025 Vidyut Prabakaran

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

from PIL import Image
import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(script_dir, 'images')

def natural_key(string):
    return [int(s) if s.isdigit() else s.lower() for s in re.split(r'(\d+)', string)]

print ("FusionPDF - Quickly convert multiple images into a single PDF document.\n")
print (" - Place the images you want to convert into the 'images' folder.")
print (" - Name the images in the order you want them to appear in the PDF (e.g., 1.jpg, 2.jpg, ...).\n")
a=input("Press Enter when ready to convert...")

print("Sorting images... (Make sure their filenames are numbered.)\n")
image_files = sorted([
    f for f in os.listdir(image_folder)
    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp'))
], key=natural_key)

print("Verifying if the files are images...\n")
if not image_files:
    print("No images found in the 'images' folder.")
    exit()

print("Converting the images to RGB...\n")
image_paths = [os.path.join(image_folder, f) for f in image_files]
images = [Image.open(p).convert('RGB') for p in image_paths]

output_path = os.path.join(script_dir, 'output.pdf')
images[0].save(output_path, save_all=True, append_images=images[1:])

print(f"Saved {len(images)} images as {output_path}")
