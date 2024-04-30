from PIL import Image, ImageSequence
import numpy as np

def generate_fractal(image_path, iterations, scale_factor, output_path):
    # Load the image
    image = Image.open(image_path)
    width, height = image.size

    # Prepare the frames list for the GIF
    frames = []

    for i in range(iterations):
        # Apply fractal transformation: Zoom in and rotate
        new_width = int(width * scale_factor ** i)
        new_height = int(height * scale_factor ** i)
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        
        # Crop to original size from center
        left = (new_width - width) // 2
        top = (new_height - height) // 2
        right = left + width
        bottom = top + height
        cropped_image = resized_image.crop((left, top, right, bottom))

        # Rotate image slightly
        rotated_image = cropped_image.rotate(i * 5)

        # Append to frames
        frames.append(rotated_image)

    # Save the frames as a GIF
    frames[0].save(output_path, save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)

# Example usage:
generate_fractal('path_to_your_input_image.jpg', iterations=10, scale_factor=1.1, output_path='output_fractal.gif')
