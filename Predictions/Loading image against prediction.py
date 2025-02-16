#To load the image against the prediction
import os
import matplotlib.pyplot as plt
import SimpleITK as sitk

# Define the paths to the images and predictions directories
images_dir = '/content/nnUNetFrame/dataset/nnUNet_raw/Dataset001_BreastTumor/imagesTs'
predictions_dir = '/content/nnUNetFrame/dataset/nnUNet_results/Dataset001_BreastTumor/nnUNet_predictions'

# List all files in the images directory
image_files = os.listdir(images_dir)
image_files.sort()

# List all files in the predictions directory
prediction_files = os.listdir(predictions_dir)
prediction_files.sort()

# Visualize each image and its corresponding prediction
for image_file, prediction_file in zip(image_files, prediction_files):
    # Load the image and prediction using SimpleITK
    image_path = os.path.join(images_dir, image_file)
    image = sitk.ReadImage(image_path)

    prediction_path = os.path.join(predictions_dir, prediction_file)
    prediction = sitk.ReadImage(prediction_path)

    # Convert SimpleITK images to numpy arrays
    image_array = sitk.GetArrayFromImage(image)
    prediction_array = sitk.GetArrayFromImage(prediction)

    # Plot the image and prediction side by side
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Display the image
    axes[0].imshow(image_array, cmap='gray')
    axes[0].set_title('Image')
    axes[0].axis('off')

    # Display the prediction
    axes[1].imshow(prediction_array, cmap='gray')
    axes[1].set_title('Prediction')
    axes[1].axis('off')

    plt.show()
