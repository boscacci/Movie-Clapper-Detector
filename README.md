# Film Slate Detector
    
My first computer vision object detection project.

I used to work night shifts in film production, scrubbing through thousands of clips to find the exact moment the clapper shut. This repo is my attempt to automate that tedious workflow (built in roughly ~64 hours of focused work).

<img src="media/tweet_thread.png" 
 alt="Project Overview" 
 height="500"
/>

***

## Overview

This project automates the detection of film clapperboards (slates) in video frames using deep learning object detection models. Originally motivated by the tedious task of manually finding clapper moments in thousands of video clips during night shifts in film production, this project demonstrates an end-to-end computer vision workflow—from data collection to model deployment.

### Notebooks

**Training Notebook** ([Training.ipynb](https://github.com/boscacci/Movie-Clapper-Detector/blob/main/notebooks/Training.ipynb)): 
- Trains an object detection model using the IceVision framework
- Uses a custom dataset of 224 labeled images in COCO format
- Supports multiple model architectures (EfficientDet, Faster R-CNN, RetinaNet, etc.)
- Includes data augmentation and validation
- Exports trained model checkpoints

**Inference Notebook** ([Inference.ipynb](https://github.com/boscacci/Movie-Clapper-Detector/blob/main/notebooks/Inference.ipynb)):
- Loads trained model checkpoints
- Runs predictions on new images
- Visualizes bounding box detections
- Exports predictions in COCO annotation format

## Development Process

### 1. Data Collection
Collected initial training dataset of 50+ slate images from instructional videos using browser screenshot tools. The dataset was iteratively expanded through active learning (see the “Active Learning Loop” section below).

### 2. Annotation with LabelStudio
Set up LabelStudio via Docker for local annotation work. This open-source tool provided an efficient interface for drawing bounding boxes around slates in training images.

### 3. Data Versioning with DVC
Implemented [DVC (Data Version Control)](https://dvc.org/) to version-control the dataset and sync training data to S3, enabling reproducible experiments and collaboration.

### 4. Cloud Infrastructure
Provisioned AWS EC2 `g4dn.xlarge` [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) for GPU-accelerated training. Used Terraform for infrastructure-as-code to make spinning up and tearing down compute resources quick and cost-effective.

### 5. Model Training with IceVision
Leveraged the [IceVision](https://airctic.com/0.7.0/install/) framework for rapid experimentation. IceVision provides unified abstractions over multiple object detection libraries (FastAI, PyTorch TorchVision, MMDetection), making it easy to try different architectures.

### 6. Experiment Tracking
Integrated Weights & Biases (WandB) for experiment tracking across different model architectures and hyperparameters. This made it straightforward to compare:
- Faster R-CNN
- YOLOv5
- EfficientDet
- VFNet

Results showed Faster R-CNN provided superior performance for this use case. Each training run took approximately 8 minutes on the g4dn.xlarge instance.

### 7. Active Learning Loop
Implemented an iterative improvement process:
1. Train model on current labeled dataset
2. Use model to auto-label new images
3. Manually review and correct erroneous predictions
4. Retrain model with expanded dataset
5. Repeat

This active learning approach efficiently scaled the dataset from 50 to 224+ labeled images while maintaining high annotation quality.

## Try it Out

**Demo:** [Film Slate Binary Classifier on Hugging Face](https://huggingface.co/spaces/cinemarob1/Film-slate-or-nah)

*Note: This demo uses a simpler binary classifier that determines whether a slate is present in an image (yes/no), rather than the full object detection model that draws bounding boxes around slates.*

***

Images labeled in Heartex LabelStudio:

<img src="media/labeled_slates.png" 
     alt="Labeling Images" 
     height="500"
/>