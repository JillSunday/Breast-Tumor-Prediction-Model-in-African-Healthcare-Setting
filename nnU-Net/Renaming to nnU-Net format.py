#Rename the images and masks in the nnUNet format
import os

# Directory containing the nifti images and masks
images_dir = "/content/nnUNetFrame/dataset/nnUNet_raw/nnUNet_raw_data/nifti_images"
masks_dir = "/content/nnUNetFrame/dataset/nnUNet_raw/nnUNet_raw_data/nifti_masks"

# Iterate over the range of indices from 1 to 262
for i in range(1, 263):
    # Construct the filenames for images and labels
    image_filename = f"BT_{i:03d}_0000.nii.gz"
    mask_filename = f"BT_{i:03d}.nii.gz"

    # Construct the full paths for images and masks
    image_old_path = os.path.join(images_dir, f"case{i:03d}.nii.gz")
    mask_old_path = os.path.join(masks_dir, f"case{i:03d}_tumor.nii.gz")

    image_new_path = os.path.join(images_dir, image_filename)
    mask_new_path = os.path.join(masks_dir, mask_filename)

    # Skip if the image file or mask file does not exist
    if not os.path.exists(image_old_path) or not os.path.exists(mask_old_path):
        print(f"Image or mask file does not exist for case{i:03d}. Skipping... duuuhhh")
        continue

    # Skip if the mask file ends with _other1.nii.gz, _other2.nii.gz, _other3.nii.gz, or _other4.nii.gz
    if mask_old_path.endswith("_other1.nii.gz") or mask_old_path.endswith("_other2.nii.gz") or mask_old_path.endswith("_other3.nii.gz") or mask_old_path.endswith("_other4.nii.gz"):
        print(f"Mask file {mask_old_path} ends with _otherX.nii.gz. Skipping...  obviously")
        continue

    # Rename the images and masks
    os.rename(image_old_path, image_new_path)
    os.rename(mask_old_path, mask_new_path)

print("Renaming completed.")



##To delete files that start with 'case' because indiscrepancies ie, no corresponding masks, or too many corresponding mask (ie. those that have been skipped)
# Directory containing the nifti images and masks
images_dir = "/content/nnUNetFrame/dataset/nnUNet_raw/nnUNet_raw_data/nifti_images"
masks_dir = "/content/nnUNetFrame/dataset/nnUNet_raw/nnUNet_raw_data/nifti_masks"

# Delete files starting with 'case' in nifti_images directory
for filename in os.listdir(images_dir):
    if filename.startswith("case"):
        file_path = os.path.join(images_dir, filename)
        os.remove(file_path)

# Delete files starting with 'case' in nifti_masks directory
for filename in os.listdir(masks_dir):
    if filename.startswith("case"):
        file_path = os.path.join(masks_dir, filename)
        os.remove(file_path)

print("Deletion completed. Easier work wooohooo!")
