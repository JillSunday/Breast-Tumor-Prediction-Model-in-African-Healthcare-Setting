#To load the image and the corresponding label against their prediction for confirmation of results.
import os
import matplotlib.pyplot as plt
import SimpleITK as sitk

# Define the paths to the images, predictions, and labels directories
images_dir = '/content/nnUNetFrame/dataset/nnUNet_raw/Dataset001_BreastTumor/imagesTs'
predictions_dir = '/content/nnUNetFrame/dataset/nnUNet_results/Dataset001_BreastTumor/nnUNet_predictions'
labels_dir = '/content/nnUNetFrame/dataset/nnUNet_raw/nnUNet_raw_data/nifti_labels'

# List all files in the images directory
image_files = os.listdir(images_dir)
image_files.sort()

# List all files in the predictions directory
prediction_files = os.listdir(predictions_dir)
prediction_files.sort()

# List all files in the labels directory
label_files = os.listdir(labels_dir)
label_files.sort()

# Visualize each image, prediction, and label
for image_file, prediction_file, label_file in zip(image_files, prediction_files, label_files):
    # Load the image, prediction, and label using SimpleITK
    image_path = os.path.join(images_dir, image_file)
    image = sitk.ReadImage(image_path)

    prediction_path = os.path.join(predictions_dir, prediction_file)
    prediction = sitk.ReadImage(prediction_path)

    label_path = os.path.join(labels_dir, label_file)
    label = sitk.ReadImage(label_path)

    # Convert SimpleITK images to numpy arrays
    image_array = sitk.GetArrayFromImage(image)
    prediction_array = sitk.GetArrayFromImage(prediction)
    label_array = sitk.GetArrayFromImage(label)

    # Plot the image, prediction, and label side by side
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Display the image
    axes[0].imshow(image_array, cmap='gray')
    axes[0].set_title('Image')
    axes[0].axis('off')

    # Display the prediction
    axes[1].imshow(prediction_array, cmap='gray')
    axes[1].set_title('Prediction')
    axes[1].axis('off')

    # Display the label
    axes[2].imshow(label_array, cmap='gray')
    axes[2].set_title('Label')
    axes[2].axis('off')

    plt.show()
