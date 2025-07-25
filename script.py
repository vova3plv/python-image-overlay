import os
from PIL import Image

# Constants
INPUT_IMG_DIR = 'img'
OUTPUT_IMG_DIR = 'output'
MAIN_IMAGE_NAME = 'images.jpg'
OPACITY_PERCENTAGE = 90
SCALE_PERCENTAGE = 75

def process_images():
    
    # Check if input and output directories exist, create output directory if not
    if not os.path.exists(INPUT_IMG_DIR):
        print(f"Input directory '{INPUT_IMG_DIR}' does not exist.")
        return
    if not os.path.exists(OUTPUT_IMG_DIR):
        os.makedirs(OUTPUT_IMG_DIR)
        print(f"Output directory '{OUTPUT_IMG_DIR}' created.")
        
    # Get all images in the input directory
    all_images = [f for f in os.listdir(INPUT_IMG_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not all_images:
        print("No images found in the input directory.")
        return
    
    if MAIN_IMAGE_NAME not in all_images:
        print(f"Main image '{MAIN_IMAGE_NAME}' not found in input directory.")
        return
    
    main_image_path = os.path.join(INPUT_IMG_DIR, MAIN_IMAGE_NAME)
    main_image = Image.open(main_image_path).convert("RGBA")
    
    # Set the opacity for the main image
    if OPACITY_PERCENTAGE < 0 or OPACITY_PERCENTAGE > 100:
        print("Opacity percentage must be between 0 and 100.")
        return
    
    opacity = int(255 * (OPACITY_PERCENTAGE / 100))
    main_image.putalpha(opacity)
    
    # Get background images
    background_images = [f for f in all_images if f != MAIN_IMAGE_NAME] 
    
    if not background_images:
        print("No background images found for processing.")
        return
    
    # Process each background image
    for i, bg_image_name in enumerate(background_images):
        bg_image_path = os.path.join(INPUT_IMG_DIR, bg_image_name)
        bg_image = Image.open(bg_image_path).convert("RGBA")
        
        # Resize the main image
        if SCALE_PERCENTAGE < 0 or SCALE_PERCENTAGE > 100:
            print("Scale percentage must be between 0 and 100.")
            return
        
        new_width = int(bg_image.width * (SCALE_PERCENTAGE / 100))
        new_height = int(bg_image.height * (SCALE_PERCENTAGE / 100))
        main_image_resized = main_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Paste the resized main image to bg_image
        paste_x = (bg_image.width - new_width) // 2
        paste_y = (bg_image.height - new_height) // 2
        
        bg_image.paste(main_image_resized, (paste_x, paste_y), main_image_resized)
        
        # Save the processed image
        output_filename = f"output_{i+1}.png"
        output_path = os.path.join(OUTPUT_IMG_DIR, output_filename)
        bg_image.save(output_path, format='PNG')
        print(f"Processed image saved as '{output_filename}' in '{OUTPUT_IMG_DIR}'.")
        
    print("Image processing completed successfully.")
    
if __name__ == "__main__":
    process_images()