#Clone nnUNet into your environment
!git clone https://github.com/MIC-DKFZ/nnUNet.git /content/nnUNetFrame/nnUNet
%cd /content/nnUNetFrame/nnUNet
!pip install -e .
!pip install numpy scipy SimpleITK batchgenerators

#Install hidden layer
nnunet_dir = '/content/nnUNetFrame/nnUNet'
os.chdir(nnunet_dir)
!pip install --upgrade git+https://github.com/FabianIsensee/hiddenlayer.git


