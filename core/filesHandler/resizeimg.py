from PIL import Image
from io import BytesIO

def compress_to_webp(image):
    """
    Compresses an image to WebP format.
    
    Parameters:
    - image: The image file object (e.g., request.FILES['image_upload']).
    
    Returns:
    - Compressed image data as bytes.
    """
    with Image.open(image) as img:
        # Compress the image to WebP format with the desired quality
        img = img.convert("RGB")  # Ensure the image is in RGB mode
        img_io = BytesIO()  # Create an in-memory file object
        img.save(img_io, format='WEBP', quality=60)  # Save the compressed image to the in-memory file
        img_io.seek(0)  # Reset the file pointer to the beginning of the file
        return img_io.getvalue()  # Return the compressed image data as bytes
