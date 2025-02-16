#Required module
#pip install openpyxl

import pandas as pd
import cv2

#define .xlsx filename and folder containing images and masks
info_filename = r'BrEaST-Lesions-USG-clinical-data-Sep-2023-with-data-dictionary-v2-Nov-7-2023.xlsx'
images_and_masks_foldername = r'BrEaST-Lesions_USG-images_and_masks/'

#read .xlsx file with clinical data
breast_dataset = pd.read_excel(info_filename, sheet_name='BrEaST-Lesions-USG clinical dat')


#read image
breast_dataset.at[i, 'Image_filename']  = cv2.imread(images_and_masks_foldername+breast_dataset.loc[i,'Image_filename'], cv2.IMREAD_UNCHANGED)


# Read the grayscale image
gray_image = cv2.imread(images_and_masks_foldername + breast_dataset.loc[i, 'Mask_tumor_filename'], cv2.IMREAD_GRAYSCALE)

# Threshold the grayscale image to generate a binary mask
_, binary_mask = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY)

# Store the binary mask in the dataset
breast_dataset.at[i, 'Mask_tumor_filename'] = binary_mask


#read other mask
if not isinstance(breast_dataset.loc[i,'Mask_other_filename'], float):
        masks_bool = []
        for mask_path in breast_dataset.loc[i,'Mask_other_filename'].split('&'):
            masks_bool.append(cv2.imread(images_and_masks_foldername+mask_path, cv2.IMREAD_GRAYSCALE)>0)
        breast_dataset.at[i, 'Mask_other_filename'] = masks_bool
else:
        breast_dataset.at[i, 'Mask_other_filename'] = []


#columns rename
breast_dataset.rename(columns={"Image_filename": "Image", "Mask_tumor_filename": "Mask_tumor", "Mask_other_filename": "Mask_other"})

#To visualize data
import matplotlib.pyplot as plt

def visualize_images(image_paths, titles=None):
    num_images = len(image_paths)
    fig, axes = plt.subplots(1, num_images, figsize=(10, 5))
    for i, image_path in enumerate(image_paths):
        try:
            image = cv2.imread(image_path)
            if image is not None:
                axes[i].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                axes[i].axis('off')
                if titles is not None:
                    axes[i].set_title(titles[i])
            else:
                print(f"Error reading image: {image_path}")
        except Exception as e:
            print(f"Error processing image: {image_path}\n{str(e)}")
    plt.show()

# Example usage
image_paths = [
    '/content/drive/MyDrive/BrEaST-Lesions_USG-images_and_masks/case251_tumor.png',
    '/content/drive/MyDrive/BrEaST-Lesions_USG-images_and_masks/case251.png',
    '/content/drive/MyDrive/BrEaST-Lesions_USG-images_and_masks/case088.png'
]
titles = ['Image 1', 'Image 2', 'Image 3']  # Optional titles for the images
visualize_images(image_paths, titles)



#Code to check the size of an image
# Load the image
image_path = '/content/drive/MyDrive/BrEaST-Lesions_USG-images_and_masks/case068_tumor.png'
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is not None:
    # Get the dimensions of the image
    height, width, channels = image.shape
    print(f"Image dimensions: Height={height}, Width={width}, Channels={channels}")
else:
    print("Error: Failed to load the image.")
