# HOG Based Chain Snatching Detection for Surveillance Systems  
### Description:
The Chain Snatching Detection in Surveillance System is a project that aims to detect chain snatching incidents in surveillance videos. The project utilizes computer vision techniques and machine learning algorithms to identify potential chain snatching events.
### Dataset
The dataset consists of frames extracted from custom-created chain snatching videos. To avoid frame duplication, some continuous frames were skipped during the extraction process.
I would suggest To create the custom dataset by considiring the different Scenarios like chain snatching on bike , on road, in crowded region  


### Block Diagram
![img.png](img.png)
### Key Techniques and Algorithms:

- Canny Edge Detection: Canny edge detection is employed to extract edges from the surveillance video frames. It helps in identifying the boundaries of objects, including chains, in the video.

- Scale-Invariant Feature Transform (SIFT): SIFT is used for feature extraction from the video frames. It helps in detecting and describing distinctive features in the images, which can be used to match and track objects.

- Histogram of Oriented Gradients (HOG): HOG feature extraction technique is applied to capture the shape and gradient information of the objects in the video frames. It helps in detecting and representing the shape and appearance of chains.

- K-means Clustering: K-means clustering is used to perform feature reduction on the SIFT feature vectors. It helps in grouping similar features together and reducing the dimensionality of the feature space.

- Principal Component Analysis (PCA): PCA is applied to reduce the dimensionality of the HOG feature vectors. It helps in capturing the most important features and removing redundant information.

### Classifiers used:
The project employs the following classifiers to train and evaluate the chain snatching detection model with k fold cross validation and hyperparameter tuning

- Support Vector Machine (SVM)
- Random Forest
- Decision Tree
- Logistic Regression
- XGBoost

Each classifier is trained on the extracted features and used for classification and prediction of chain snatching events.

## Dependencies:
- numpy
- pandas
- opencv-python
- matplotlib.
- scikit-learn
- rembg

## Installation
    - Download the dataset form the given link
    - Install the dependencies
    - First run the BG_Remove.py to remove the background form the images and save in rembg folder
    - After run the both the ipynb file SIFT and HOG 


*Note* - HOG Featrure extraction technique has shown the accurate result #
