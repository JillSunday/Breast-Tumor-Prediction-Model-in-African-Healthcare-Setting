#This is to merge the resized_images and synthesized_ood
import os
import shutil

# Define paths
resized_images_directory = '/content/resized_images'
synthesized_data_directory = '/content/synthesized_data'
merged_dataset_directory = '/content/merged_dataset'
merged_images_directory = os.path.join(merged_dataset_directory, 'merged_images')
merged_masks_directory = os.path.join(merged_dataset_directory, 'merged_masks')

# Create merged_dataset_directory if it doesn't exist
os.makedirs(merged_dataset_directory, exist_ok=True)
os.makedirs(merged_images_directory, exist_ok=True)
os.makedirs(merged_masks_directory, exist_ok=True)

# Copy images from resized_images/images to merged_dataset/merged_images
for filename in os.listdir(os.path.join(resized_images_directory, 'images')):
    src = os.path.join(resized_images_directory, 'images', filename)
    dst = os.path.join(merged_images_directory, filename)
    shutil.copy(src, dst)
    print(f"Copied image: {filename} to merged_images")

# Copy images from synthesized_data/ood_images to merged_dataset/merged_images
for filename in os.listdir(os.path.join(synthesized_data_directory, 'ood_images')):
    src = os.path.join(synthesized_data_directory, 'ood_images', filename)
    dst = os.path.join(merged_images_directory, filename)
    shutil.copy(src, dst)
    print(f"Copied image: {filename} to merged_images")

# Copy masks from resized_images/masks to merged_dataset/merged_masks
for filename in os.listdir(os.path.join(resized_images_directory, 'masks')):
    src = os.path.join(resized_images_directory, 'masks', filename)
    dst = os.path.join(merged_masks_directory, filename)
    shutil.copy(src, dst)
    print(f"Copied mask: {filename} to merged_masks")

# Copy masks from synthesized_data/ood_masks to merged_dataset/merged_masks
for filename in os.listdir(os.path.join(synthesized_data_directory, 'ood_masks')):
    src = os.path.join(synthesized_data_directory, 'ood_masks', filename)
    dst = os.path.join(merged_masks_directory, filename)
    shutil.copy(src, dst)
    print(f"Copied mask: {filename} to merged_masks")

print("Merge completed successfully.")
