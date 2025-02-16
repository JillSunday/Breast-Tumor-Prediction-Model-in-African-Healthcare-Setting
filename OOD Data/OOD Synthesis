#To synthesize ood data, using the last 6 images and masks from resized_images directory
import os
import shutil
import imgaug.augmenters as iaa
from PIL import Image
import numpy as np

# Define paths
resized_images_directory = '/content/resized_images'
synthesized_data_directory = '/content/synthesized_data'
ood_images_directory = os.path.join(synthesized_data_directory, 'ood_images')
ood_masks_directory = os.path.join(synthesized_data_directory, 'ood_masks')

# Ensure directories exist
os.makedirs(ood_images_directory, exist_ok=True)
os.makedirs(ood_masks_directory, exist_ok=True)

# Get the last 6 images and masks
image_files = sorted(os.listdir(os.path.join(resized_images_directory, 'images')))[-6:]
mask_files = sorted(os.listdir(os.path.join(resized_images_directory, 'masks')))[-6:]

# Define augmentation pipeline
augmentation_pipeline = iaa.Sequential([
    iaa.Affine(rotate=(-10, 10)),  # Rotate images randomly between -10 to 10 degrees
    iaa.GaussianBlur(sigma=(0.0, 1.5)),  # Apply Gaussian blur with a sigma between 0.0 to 1.5
    iaa.AdditiveGaussianNoise(scale=(0, 0.075*255)),  # Add Gaussian noise with a scale of 0 to 0.075 times 255
])

# Synthesize OOD examples
for image_file, mask_file in zip(image_files, mask_files):
    src_image = os.path.join(resized_images_directory, 'images', image_file)
    src_mask = os.path.join(resized_images_directory, 'masks', mask_file)
    dst_image = os.path.join(ood_images_directory, image_file)
    dst_mask = os.path.join(ood_masks_directory, mask_file)

    # Augment image
    image = Image.open(src_image)
    augmented_image = augmentation_pipeline(image=np.array(image))
    augmented_image = Image.fromarray(augmented_image)

    # Copy augmented image and mask to ood directories
    augmented_image.save(dst_image)
    shutil.copy(src_mask, dst_mask)

print("OOD images and masks synthesized successfully with augmentation.YAAAAYYYYY!!!!")




#To visualize 5 images from ood_images subdirectory
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Define the path to the ood_images subdirectory
ood_images_directory = '/content/synthesized_data/ood_images'

# Get a list of all files in the ood_images subdirectory
ood_image_files = os.listdir(ood_images_directory)

# Select the first 5 image files
selected_ood_images = ood_image_files[:5]

# Visualize the selected images
plt.figure(figsize=(15, 8))
for i, filename in enumerate(selected_ood_images, 1):
    img_path = os.path.join(ood_images_directory, filename)
    img = mpimg.imread(img_path)
    plt.subplot(1, 5, i)
    plt.imshow(img)
    plt.title(filename)
    plt.axis('off')

plt.show()
