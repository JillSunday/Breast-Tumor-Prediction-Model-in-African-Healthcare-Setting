import json

def generate_dataset_json(output_file, channel_names, labels, dataset_name, description, reference, release, license, additional_params, num_training, file_ending):
    dataset_info = {
        "channel_names": channel_names,
        "labels": labels,
        "dataset_name": dataset_name,
        "description": description,
        "reference": reference,
        "release": release,
        "license": license,
        "additional_params": additional_params,
        "numTraining": num_training,
        "file_ending": file_ending
    }

    with open(output_file, 'w') as f:
        json.dump(dataset_info, f, indent=4)

# Define dataset information
channel_names = {
    0: 'ultrasound'  # Since breast ultrasound scans are typically grayscale images, there is only one channel
}
labels = {
    'background': 0,  #blue
    'tumor': 1,  #red
}
dataset_name = 'BrEast-Lesions_USG_images_and_masks'
description = """Dataset containing breast ultrasound scans with labels and annotations.
Preprocessing:
- Resizing: Images were resized to a fixed resolution of (256, 256) to standardize the input size for the neural network model.
- Augmentation: Augmentation techniques such as rotation, flipping, and adding Gaussian and K- noise were applied to increase dataset diversity and improve model generalization.
"""
reference = 'Pawłowska, A., Ćwierz-Pieńkowska, A., Domalik, A., Jaguś, D., Kasprzak, P., Matkowski, R., Fura, Ł., Nowicki, A., & Zolek, N. (2024). A Curated Benchmark Dataset for Ultrasound Based Breast Lesion Analysis (Breast-Lesions-USG) (Version 1) [dataset]. The Cancer Imaging Archive. https://doi.org/10.7937/9WKK-Q141'
release = '2024/01/08'  # Update date of the dataset
license_name = 'CC by 4.0'
license_url = 'https://creativecommons.org/licenses/by/4.0/'
license = f'Licensed under {license_name}. For more details, see {license_url}'
additional_params = {
    'patient_labels_file': '/content/BrEaST-Lesions-USG-clinical-data-Sep-2023-with-data-dictionary-v2-Nov-7-2023.xlsx',
}
num_training = 206
file_ending = '.nii.gz'

# Generate dataset JSON file
generate_dataset_json('/content/nnUNetFrame/dataset/nnUNet_raw/Dataset001_BreastTumor/dataset.json',
                      channel_names=channel_names,
                      labels=labels,
                      dataset_name=dataset_name,
                      description=description,
                      reference=reference,
                      release=release,
                      license=license,
                      additional_params=additional_params,
                      num_training=num_training,
                      file_ending=file_ending)
