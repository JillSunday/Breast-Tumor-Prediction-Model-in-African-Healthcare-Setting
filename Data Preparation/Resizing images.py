#Resizing the images to 256 x 256

def resize_images(input_folder, output_folder, target_size=(256, 256)):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over the images in the input folder
    for filename in os.listdir(input_folder):
        # Read the image
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        # Resize the image
        resized_img = cv2.resize(img, target_size)

        # Save the resized image to the output folder
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, resized_img)

# Example usage
input_folder = '/content/drive/MyDrive/BrEaST-Lesions_USG-images_and_masks'
output_folder = '/content/resized_images'
resize_images(input_folder, output_folder)


#To check if image has been resized
# Load the image
image_path = '/content/resized_images/case077_tumor.png'
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is not None:
    # Get the dimensions of the image
    height, width, channels = image.shape
    print(f"Image dimensions: Height={height}, Width={width}, Channels={channels}")
else:
    print("Error: Failed to load the image.")

