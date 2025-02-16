
# Breast Tumor Segmentation in Low-Resource African Healthcare Settings 🏥 (Accepted for presentation at the Deep Learning Indaba 2024, Dakar, Senegal)

This project addresses the challenge of breast tumor segmentation in African healthcare environments, where limited access to high-quality imaging devices and datasets hinders robust model development. Using a curated ultrasound dataset and synthetic out-of-distribution (OOD) data augmentation, we demonstrate the efficacy of nnU-Net for tumor segmentation under resource-constrained conditions.

## Table of Contents
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Methodology](#methodology)
  - [Data Preparation](#data-preparation)
  - [OOD Data Generation](#ood-data-generation)
  - [Model Training](#model-training)
- [Results](#results)
- [Predictions](#predictions)
- [References](#references)
- [Notebooks](#notebooks)
- [License](#license)

---

## Dataset
### Original Dataset
The project utilizes the **Breast-Lesions-USG** dataset from [The Cancer Imaging Archive (TCIA)](https://www.cancerimagingarchive.net/collection/breast-lesions-usg/):  
**Citation**:  
Pawłowska, A., et al. (2024). A Curated Benchmark Dataset for Ultrasound Based Breast Lesion Analysis (Breast-Lesions-USG) (Version 1) [dataset]. The Cancer Imaging Archive. [DOI: 10.7937/9WKK-Q141](https://doi.org/10.7937/9WKK-Q141).

### Curated Dataset
To simplify multi-tumor annotations, we removed auxiliary masks (e.g., `casenumber_other1.png`). The curated dataset is available on [Google Drive](https://drive.google.com/drive/folders/16hZbKotB_fjsvG79W_iFMuyvGLBbJFLt?usp=drive_link). The synthetic OOD generation code is located in the 'OOD Data' folder

---

## Project Structure
Breast-Tumor-Prediction-Model-in-African-Healthcare-Setting/
│
├── Data/ # Raw and curated datasets
├── Data Preparation/ # Scripts for Resizing and folder arrangment of data
├── OOD Data/ # Synthetic African-like ultrasound images
├── Data Merger/ # Code for merging OOD and original data
├── nnU-Net/ # nnU-Net configuration files
├── Training/ # Training scripts 
├── Predictions/ # Model predictions on test data
├── Results/ # Visualizations and metrics
├── requirements.txt # Python dependencies
├── LICENSE # MIT License
└── .gitignore # Excluded files (data, logs, etc.)

---

## Methodology
### Data Preparation
To address multi-tumor annotations, we retained only the primary mask (`casenumber_tumor.png`) and removed auxiliary masks (`casenumber_other1.png`, etc.). This simplification ensures compatibility with nnU-Net’s segmentation framework.  
**Data Visualization**:  
![Data Loading](https://github.com/JillSunday/Breast-Tumor-Prediction-Model-in-African-Healthcare-Setting/blob/main/Results/Data%20Visualization%20after%20data%20loading.png?raw=true)

### OOD Data Generation
To simulate African healthcare imaging conditions, we augmented 6 training images using the `imgaug` library. The augmentation pipeline included the following transformations:  
- **Rotation**: Randomly rotated images between -10° to 10° (`iaa.Affine(rotate=(-10, 10))`).  
- **Gaussian Blur**: Applied Gaussian blur with a sigma range of 0.0 to 1.5 (`iaa.GaussianBlur(sigma=(0.0, 1.5))`).  
- **Gaussian Noise**: Added Gaussian noise with a scale of 0 to 0.075 times 255 (`iaa.AdditiveGaussianNoise(scale=(0, 0.075*255))`).  

This pipeline generated synthetic OOD data to improve model generalizability without overfitting to African-specific artifacts.  

**Augmentation Examples**:  
![OOD Data](https://github.com/JillSunday/Breast-Tumor-Prediction-Model-in-African-Healthcare-Setting/blob/main/Results/Examples%20of%20OOD%20data%20after%20data%20augmentation%20using%20imgaug.png?raw=true)

### Model Training
We trained nnU-Net v2 on the merged dataset (original + OOD data) for 57 epochs. Labels were generated via mask thresholding.  
**Training Progress**:  
![Pseudo Dice](https://github.com/JillSunday/Breast-Tumor-Prediction-Model-in-African-Healthcare-Setting/blob/main/Results/Visual%20evidence%20of%20best%20Pseudo%20Dice%20at%2055%20epochs%20of%20training.png?raw=true)  
**Best Pseudo Dice**: **0.9616 at 55 epochs** (Validation Set)

---

## Results
The model successfully segmented tumors in images with historical multi-mask annotations, despite training on simplified labels:  
1. **Multi-Tumor Prediction**:  
![Multiple Tumors](https://github.com/JillSunday/Breast-Tumor-Prediction-Model-in-African-Healthcare-Setting/blob/main/Results/Multiple%20preds4.png?raw=true)  
2. **Single-Tumor Ground Truth vs. Multi-Tumor Prediction**:  
![Prediction Comparison](https://github.com/JillSunday/Breast-Tumor-Prediction-Model-in-African-Healthcare-Setting/blob/main/Results/Example%204%20of%20prediction%20multiple%20tumors,%20with%20one%20tumor%20in%20the%20label.png?raw=true)

---
 ## Breast Tumor Segmentation notebooks
Click [here](https://colab.research.google.com/drive/1KUF-kezL-7IKZ5ILzuAnLusjez7G64A8?usp=sharing) to open the notebook in Google Colab.
  
The Python implementation of the model is available in [`python_script.py`](Notebook/breast_tumor_ultrasound_image_segmentation.py).
 

## References
### Dataset
Pawłowska, A., et al. (2024). A Curated Benchmark Dataset for Ultrasound Based Breast Lesion Analysis (Breast-Lesions-USG). The Cancer Imaging Archive. [DOI: 10.7937/9WKK-Q141](https://doi.org/10.7937/9WKK-Q141).

### nnU-Net
Isensee, F., et al. (2021). nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. *Nature Methods*, 18(2), 203–211. [DOI: 10.1038/s41592-020-01008-z](https://doi.org/10.1038/s41592-020-01008-z).

### imgaug
Jung, A. B., et al. (2020). imgaug. GitHub Repository. [https://github.com/aleju/imgaug](https://github.com/aleju/imgaug).

---

## License
This project is licensed under the [MIT License](https://github.com/JillSunday/Breast-Tumor-Prediction-Model-in-African-Healthcare-Setting/blob/main/LICENSE).  
**Code Exclusion**: See [.gitignore](https://github.com/JillSunday/Breast-Tumor-Prediction-Model-in-African-Healthcare-Setting/blob/main/.gitignore) for omitted files.
