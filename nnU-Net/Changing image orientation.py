#To change the direction of the image to match the labels(ie. (1.0, 0.0, 0.0, 1.0))
import os
import SimpleITK as sitk

# Define the desired direction for the images
desired_direction = (1.0, 0.0, 0.0, 1.0)  # Desired direction for the images

# Define the directory paths for images and masks
image_dir = '/content/nnUNetFrame/dataset/nnUNet_raw/Dataset001_BreastTumor/imagesTr'

# Get list of image files
image_files = os.listdir(image_dir)

# Iterate through each image
for image_file in image_files:
    # Load image
    image_path = os.path.join(image_dir, image_file)
    image = sitk.ReadImage(image_path)

    print(f"Loaded image: {image_file}")

    # Check if the direction of the image matches the desired direction
    if image.GetDirection() != desired_direction:
        # Resample the image to match the desired direction
        image_resampled = sitk.Resample(image, image, sitk.Transform(), sitk.sitkNearestNeighbor, 0, image.GetPixelID())

        # Update the direction of the image
        image_resampled.SetDirection(desired_direction)

        print(f"Resampled image to match desired direction: {desired_direction}")

        # Save the resampled image
        sitk.WriteImage(image_resampled, image_path)

        print(f"Saved resampled image: {image_file}")
