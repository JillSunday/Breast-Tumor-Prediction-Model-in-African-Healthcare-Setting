import os

# Define the path to the resized_images folder
resized_images_folder = '/content/resized_images'

# Define the subdirectory names for images and masks
image_subdirectory = 'images'
mask_subdirectory = 'masks'

# Check if the subdirectories exist
image_subdirectory_path = os.path.join(resized_images_folder, image_subdirectory)
mask_subdirectory_path = os.path.join(resized_images_folder, mask_subdirectory)

if os.path.exists(image_subdirectory_path):
    print(f"Subdirectory '{image_subdirectory}' exists for images.")
else:
    print(f"Subdirectory '{image_subdirectory}' does not exist for images.")

if os.path.exists(mask_subdirectory_path):
    print(f"Subdirectory '{mask_subdirectory}' exists for masks.")
else:
    print(f"Subdirectory '{mask_subdirectory}' does not exist for masks.")


#Create sub directory to the resized masks

# Define the path to the resized_images directory
resized_images_dir = '/content/resized_images'

# Define the path to the masks directory within resized_images
masks_dir = os.path.join(resized_images_dir, 'masks')

# Check if the masks directory exists, if not, create it
if not os.path.exists(masks_dir):
    os.makedirs(masks_dir)
    print("Masks directory created successfully.")
else:
    print("Masks directory already exists.")



#Define sub directory to the resized images

# Define the path to the resized_images directory
resized_images_dir = '/content/resized_images'

# Define the path to the images directory within resized_images
images_dir = os.path.join(resized_images_dir, 'images')

# Check if the images directory exists, if not, create it
if not os.path.exists(images_dir):
    os.makedirs(images_dir)
    print("Images directory created successfully.")
else:
    print("Images directory already exists.")




import os
import shutil

# Define the path to the resized_images folder
resized_images_folder = '/content/resized_images'

# Define the subdirectory names for images and masks
image_subdirectory = 'images'
mask_subdirectory = 'masks'

# Create the image subdirectory if it doesn't exist
image_subdirectory_path = os.path.join(resized_images_folder, image_subdirectory)
os.makedirs(image_subdirectory_path, exist_ok=True)

# Create the mask subdirectory if it doesn't exist
mask_subdirectory_path = os.path.join(resized_images_folder, mask_subdirectory)
os.makedirs(mask_subdirectory_path, exist_ok=True)

# Get a list of all files in the resized_images folder
all_files = os.listdir(resized_images_folder)

# Move files to their respective subdirectories
for filename in all_files:
    src = os.path.join(resized_images_folder, filename)
    if'_tumor' in filename or '_other1' in filename or '_other2' in filename:
        # Move mask files to the mask subdirectory
        dst = os.path.join(mask_subdirectory_path, filename)
        shutil.move(src, dst)
        print(f"Moved mask file: {filename} to {mask_subdirectory}")
    elif filename.endswith('.png'):
        # Move image files to the images subdirectory
        dst = os.path.join(image_subdirectory_path, filename)
        shutil.move(src, dst)
        print(f"Moved image file: {filename} to {image_subdirectory}")

print("Files have been moved to their respective subdirectories.")





#To extract masks from the images subdirectory and directing them to the masks subdirectory
import os
import shutil

# Define the path to the resized_images folder
resized_images_folder = '/content/resized_images'

# Define the subdirectory names for images and labels
image_subdirectory = 'images'
mask_subdirectory = 'masks'

# Create the image subdirectory if it doesn't exist
image_subdirectory_path = os.path.join(resized_images_folder, image_subdirectory)
os.makedirs(image_subdirectory_path, exist_ok=True)

# Create the mask subdirectory if it doesn't exist
mask_subdirectory_path = os.path.join(resized_images_folder, mask_subdirectory)
os.makedirs(mask_subdirectory_path, exist_ok=True)

# Get a list of all files in the images subdirectory
image_files = os.listdir(image_subdirectory_path)

# Move masked images to the masks subdirectory
for filename in image_files:
    if '_tumor' in filename or '_other1' in filename or '_other2' in filename or '_other3' in filename or '_other4' in filename:
        src = os.path.join(image_subdirectory_path, filename)
        dst = os.path.join(mask_subdirectory_path, filename)
        shutil.move(src, dst)
        print(f"Moved masked image file: {filename} to {mask_subdirectory}")

print("Masked images have been moved to the masks subdirectory.")




#To visualize images in the images subdirectory in the resized_images directory
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Define the path to the images subdirectory
image_subdirectory = '/content/resized_images/images'

# Get a list of all files in the images subdirectory
image_files = os.listdir(image_subdirectory)

# Select the first 5 image files
selected_images = image_files[:5]

# Visualize the selected images
plt.figure(figsize=(15, 8))
for i, filename in enumerate(selected_images, 1):
    img_path = os.path.join(image_subdirectory, filename)
    img = mpimg.imread(img_path)
    plt.subplot(1, 5, i)
    plt.imshow(img)
    plt.title(filename)
    plt.axis('off')

plt.show()




