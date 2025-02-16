import os
import SimpleITK as sitk
import numpy as np

# Define the labels for each region
Background_label = 0  # Blue
Tumor_label = 1  # Red

# Define the directory paths for masks and labels
mask_dir = '/content/nnUNetFrame/dataset/nnUNet_raw/nnUNet_raw_data/nifti_masks'
label_dir = '/content/nnUNetFrame/dataset/nnUNet_raw/nnUNet_raw_data/nifti_labels'

# Get list of mask files
mask_files = os.listdir(mask_dir)

# Iterate through each mask
for mask_file in mask_files:
    # Load mask image
    mask_path = os.path.join(mask_dir, mask_file)
    mask_img = sitk.ReadImage(mask_path)

    print(f"Loaded mask: {mask_file}")

    # Convert SimpleITK image to numpy array
    mask_np = sitk.GetArrayFromImage(mask_img)

    print("Converted mask to numpy array")

    # Create a new label image
    label_img = np.zeros_like(mask_np)

    # Assign labels to regions
    label_img[mask_np == 0] = Background_label  # Background
    label_img[mask_np != 0] = Tumor_label  # Tumor region (assuming any non-zero pixel belongs to tumor)

    print("Assigned labels to regions")

    # Save label image
    label_file = mask_file.replace('.nii.gz', '.nii.gz')  
    label_path = os.path.join(label_dir, label_file)
    label_img_nifti = sitk.GetImageFromArray(label_img)
    sitk.WriteImage(label_img_nifti, label_path)

    print(f"Saved label image: {label_file}")




#To view the newly generated label and the corresponding image
import os
import nibabel as nib
import matplotlib.pyplot as plt

# Define the directory paths for images and labels
image_dir = '/content/nnUNetFrame/dataset/nnUNet_raw/nnUNet_raw_data/nifti_images'
label_dir = '/content/nnUNetFrame/dataset/nnUNet_raw/nnUNet_raw_data/nifti_labels'

# Choose an image file to visualize (replace 'image_file' with the actual file name)
image_file = 'BT_255_0000.nii.gz'
label_file = 'BT_255.nii.gz'

# Load the image and corresponding label
image_path = os.path.join(image_dir, image_file)
label_path = os.path.join(label_dir, label_file)

image_data = nib.load(image_path).get_fdata()
label_data = nib.load(label_path).get_fdata()

# Print the shape of the image data
print("Image data shape:", image_data.shape)

# Print the shape of the label data
print("Label data shape:", label_data.shape)

# Visualize the image and label
plt.figure(figsize=(12, 6))

# Plot the image
plt.subplot(1, 2, 1)
plt.imshow(image_data, cmap='gray')
plt.title('Ultrasound Image')

# Plot the label
plt.subplot(1, 2, 2)
plt.imshow(label_data, cmap='jet', vmin=0, vmax=3)  # Assuming 4 labels
plt.title('Label Image')

plt.show()
