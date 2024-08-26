import cv2 as cv
import os
from PIL import Image, ImageDraw

def first_step(image_path):
    # Load the image and convert it to grayscale
    img = cv.imread(image_path)
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, binary_img = cv.threshold(gray_img, 240, 255, cv.THRESH_BINARY_INV)
    contours, _ = cv.findContours(binary_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        return None, None  # No dots found
    
    largest_contour = max(contours, key=cv.contourArea)
    moment = cv.moments(largest_contour)
    
    if moment["m00"] == 0:
        return None, None
    
    center_x = int(moment["m10"] / moment["m00"])
    center_y = int(moment["m01"] / moment["m00"])
    
    dot_color = img[center_y, center_x]
    
    return (center_x, center_y), dot_color

def sort_image(filenames):
    import re
    
    def extract_number(filename):
        match = re.search(r'(\d+)', filename)
        return int(match.group(0)) if match else float('inf')
    
    return sorted(filenames, key=extract_number)

def merge_images(folder_path):
    image_files = [file for file in os.listdir(folder_path) if file.endswith('.png')]
    sorted_images = sort_image(image_files)
    
    final_img = Image.new('RGB', (512, 512), (255, 255, 255))
    draw_on_img = ImageDraw.Draw(final_img)
    
    prev_pos = None
    prev_color = None
    
    for filename in sorted_images:
        file_path = os.path.join(folder_path, filename)
        
        pos, color = first_step(file_path)
        if pos is None:
            prev_pos = None
            prev_color = None
            continue
        
        if prev_pos:
            draw_on_img.line([prev_pos, pos], fill=tuple(int(c) for c in color), width=5)
        
        prev_pos = pos
        prev_color = color
    
    output_file = os.path.join(folder_path, 'final_image.png')
    final_img.save(output_file)
    print(f"Final output created and saved as {output_file}")

# Path to the folder 
image_folder = '.\\assets'
merge_images(image_folder)
