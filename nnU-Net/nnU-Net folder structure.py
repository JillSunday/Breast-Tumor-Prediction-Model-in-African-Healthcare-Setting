import os
root_dir = '/content/nnUNetFrame'
nnunet_dir = os.path.join(root_dir, 'nnUNet')
os.makedirs(nnunet_dir, exist_ok=True)
dataset_dir = os.path.join(root_dir, 'dataset')
os.makedirs(dataset_dir, exist_ok=True)
subfolders = ['nnUNet_raw', 'nnUNet_preprocessed', 'nnUNet_results']
for subfolder in subfolders:
    subfolder_path = os.path.join(dataset_dir, subfolder)
    os.makedirs(subfolder_path, exist_ok=True)
nnunet_raw_dir = os.path.join(dataset_dir, 'nnUNet_raw')
raw_subfolders = ['nnUNet_raw_data', 'nnUNet_cropped_data']
for subfolder in raw_subfolders:
    subfolder_path = os.path.join(nnunet_raw_dir, subfolder)
    os.makedirs(subfolder_path, exist_ok=True)

print("Folder structure created successfully.")
