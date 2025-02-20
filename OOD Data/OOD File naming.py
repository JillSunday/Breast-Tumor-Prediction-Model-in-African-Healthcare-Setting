import os
#Renaming the ood data such it it is a continuation from the original dataset to prevent duplicates
# Directory containing synthesized OOD images and masks
ood_images_dir = "/content/synthesized_data/ood_images"
ood_masks_dir = "/content/synthesized_data/ood_masks"

# Define the range for the new case numbers
ood_start_index = 257
ood_end_index = 262

# Initialize a counter for the OOD cases
ood_counter = 0

# Iterate over the images directory
for filename in os.listdir(ood_images_dir):
    if filename.endswith(".png"):  # Adjust the extension if necessary
        # Increment the counter
        ood_counter += 1

        # Check if the counter is within the desired range
        if 1 <= ood_counter <= 6:
            # Construct the new filename
            new_filename = f"case{ood_start_index + ood_counter - 1}.png"  # Adjust the extension if necessary
            # Construct the full paths
            old_filepath = os.path.join(ood_images_dir, filename)
            new_filepath = os.path.join(ood_images_dir, new_filename)

            # Rename the file
            os.rename(old_filepath, new_filepath)

            # Print the renaming information
            print(f"Renamed {filename} to {new_filename}")

# Reset the counter for the masks
ood_counter = 0

# Iterate over the masks directory
for filename in os.listdir(ood_masks_dir):
    if filename.endswith(".png"):
        # Increment the counter
        ood_counter += 1

        # Check if the counter is within the desired range
        if 1 <= ood_counter <= 6:
            # Construct the new filename
            new_filename = f"case{ood_start_index + ood_counter - 1}_tumor.png"
            # Construct the full paths
            old_filepath = os.path.join(ood_masks_dir, filename)
            new_filepath = os.path.join(ood_masks_dir, new_filename)

            # Rename the file
            os.rename(old_filepath, new_filepath)

            # Print the renaming information
            print(f"Renamed {filename} to {new_filename}")

print("Renaming completed.")
