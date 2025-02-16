#To split the dataset into imagesTr, labelsTr(for training) and imagesTs (for testing)
import os
import shutil
import random

# Function to split dataset
def split_dataset(images_dir, labels_dir, train_ratio=0.8, test_ratio=0.2, seed=42):
    random.seed(seed)

    # Get list of filenames
    image_filenames = os.listdir(images_dir)

    # Shuffle filenames
    random.shuffle(image_filenames)

    # Calculate number of images for each set
    num_images = len(image_filenames)
    num_train = int(train_ratio * num_images)
    num_test = num_images - num_train

    # Split filenames into sets
    train_images = image_filenames[:num_train]
    test_images = image_filenames[num_train:]

    return train_images, test_images

# Define paths
nnunet_raw_data_dir = '/content/nnUNetFrame/dataset/nnUNet_raw/nnUNet_raw_data'
nifti_images_dir = os.path.join(nnunet_raw_data_dir, 'nifti_images')
nifti_labels_dir = os.path.join(nnunet_raw_data_dir, 'nifti_labels')

# Split dataset
train_images, test_images = split_dataset(nifti_images_dir, nifti_labels_dir)

# Create Dataset001_BreastTumor Directory
nnunet_raw_dir = '/content/nnUNetFrame/dataset/nnUNet_raw'
dataset001_BreastTumor_dir = os.path.join(nnunet_raw_dir, 'Dataset001_BreastTumor')
os.makedirs(dataset001_BreastTumor_dir, exist_ok=True)

# Define directories for sets in Dataset001_BrainTumor
images_tr_dir = os.path.join(dataset001_BreastTumor_dir, 'imagesTr')
labels_tr_dir = os.path.join(dataset001_BreastTumor_dir, 'labelsTr')
images_ts_dir = os.path.join(dataset001_BreastTumor_dir, 'imagesTs')

# Create directories if they don't exist
os.makedirs(images_tr_dir, exist_ok=True)
os.makedirs(labels_tr_dir, exist_ok=True)
os.makedirs(images_ts_dir, exist_ok=True)

# Move images and labels to respective directories
for filename in train_images:
    image_src = os.path.join(nifti_images_dir, filename)
    label_src = os.path.join(nifti_labels_dir, filename.replace('_0000.nii.gz', '.nii.gz'))

    if os.path.exists(image_src) and os.path.exists(label_src):
        image_dest = os.path.join(images_tr_dir, filename)
        label_dest = os.path.join(labels_tr_dir, filename.replace('_0000.nii.gz', '.nii.gz'))
        shutil.move(image_src, image_dest)
        shutil.move(label_src, label_dest)

for filename in test_images:
    image_src = os.path.join(nifti_images_dir, filename)
    if os.path.exists(image_src):
        image_dest = os.path.join(images_ts_dir, filename)
        shutil.move(image_src, image_dest)

print("Dataset split into imagesTr, labelsTr, and imagesTs in Dataset001_BreastTumor directory.")
