#To convert images and corresponding ground truth masks to nifti format
import os
import shutil
import nibabel as nib
import numpy as np
import cv2

# Define paths
merged_dataset_directory = '/content/merged_dataset'
nnunet_raw_data_dir = '/content/nnUNetFrame/dataset/nnUNet_raw/nnUNet_raw_data'
nifti_images_dir = os.path.join(nnunet_raw_data_dir, 'nifti_images')
nifti_masks_dir = os.path.join(nnunet_raw_data_dir, 'nifti_masks')

# Function to load image data
def load_image(input_path):
    # Load image using OpenCV
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)  # Load image as grayscale
    return image

# Function to convert image or mask  to NIfTI format
def convert_to_nifti(input_directory, output_type):
    # Define output directory for NIfTI files
    output_nifti_directory = os.path.join(nnunet_raw_data_dir, f'nifti_{output_type}')

    # Create output directory for NIfTI files if it doesn't exist
    os.makedirs(output_nifti_directory, exist_ok=True)

    # Determine input directory for images or masks
    if output_type == 'images':
        input_directory = os.path.join(input_directory, 'merged_images')
    elif output_type == 'masks':
        input_directory = os.path.join(input_directory, 'merged_masks')

    # Function to convert image or mask to NIfTI format
    def convert_to_nifti_single(input_path, output_path):
        # Load image or mask data
        data = load_image(input_path)

        # Convert data type to integer (for masks)
        if output_type == 'masks':
            data = data.astype(np.int16)

        # Create NIfTI image object
        nifti_img = nib.Nifti1Image(data, np.eye(4))  # Assuming identity affine matrix

        # Save NIfTI image
        nib.save(nifti_img, output_path)
        print(f"Saved NIfTI {output_type} image: {output_path}")

    # Iterate over files in input directory
    for filename in os.listdir(input_directory):
        input_file = os.path.join(input_directory, filename)
        output_file = os.path.join(output_nifti_directory, f"{os.path.splitext(filename)[0]}.nii.gz")  # Output file path (with .nii.gz extension)
        convert_to_nifti_single(input_file, output_file)

# Convert images to NIfTI format
convert_to_nifti(merged_dataset_directory, 'images')

# Convert labels to NIfTI format
convert_to_nifti(merged_dataset_directory, 'masks')

print("Conversion completed. NIfTI files created.")

# Move NIfTI images and masks to nnUNet_raw_data directory
os.makedirs(nifti_images_dir, exist_ok=True)
os.makedirs(nifti_masks_dir, exist_ok=True)

# Move NIfTI images
for filename in os.listdir(os.path.join(nnunet_raw_data_dir, 'nifti_images')):
    source = os.path.join(nnunet_raw_data_dir, 'nifti_images', filename)
    dest = os.path.join(nifti_images_dir, filename)
    shutil.move(source, dest)

# Move NIfTI labels
for filename in os.listdir(os.path.join(nnunet_raw_data_dir, 'nifti_masks')):
    source = os.path.join(nnunet_raw_data_dir, 'nifti_masks', filename)
    dest = os.path.join(nifti_masks_dir, filename)
    shutil.move(source, dest)

print("NIfTI files moved to nnUNet_raw_data directory.")
