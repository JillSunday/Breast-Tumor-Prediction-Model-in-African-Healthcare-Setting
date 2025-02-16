import os
# Set the GPU ID (change the ID as needed)
gpu_id = 0

# Set the CUDA_VISIBLE_DEVICES environment variable
os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu_id)

# Define the argument values
dataset_name = "Dataset001_BreastTumor"
configuration = "2d"
folds = "all"
trainer = "nnUNetTrainer"
num_gpus = 1

command = f"nnUNetv2_train {dataset_name} {configuration} {folds} -tr {trainer} -num_gpus {num_gpus} --npz --val_best --c"

# Run the command
!{command}
