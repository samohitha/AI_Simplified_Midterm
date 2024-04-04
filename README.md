# Simplified Midterm Project

**Project Presentation Link:** [Click here to watch the presentation]()

## Introduction
This project demonstrates the process of training, testing, and deploying a SKLearn model on AWS SageMaker, accessible through a web application client.

## Model and Data
The model source and associated files can be downloaded from [this link](https://storage.googleapis.com/aiec-s24/4-%20Training%20a%20Static%20Malware%20Detector.zip). The provided code originates from Lab 5.4, featuring pre-existing training code and a dataset of labeled PE files. The utilized model in this project is the RandomForestClassifier.

## Deployment
Models generated from Lab 5.4 are dumped and imported via the Joblib library. An inference script is subsequently created to be utilized on the AWS SageMaker endpoint, processing input (PE features) from the client application. All dependencies are listed in requirements.txt for SageMaker to detect and install any missing packages. These components are then compressed into a model.tar.gz file, which is uploaded to an S3 bucket for deployment. An endpoint is created using the uploaded zip file.

## Client
A client web application is developed using Streamlit in Python, executed in Google Colab. Users can upload a .exe file into the application. The backend code extracts PE features from the uploaded files and packs them into a JSON format, which is then pushed to the endpoint for prediction. The application records the response from the endpoint and displays the classification of the uploaded .exe file.

## File Structure in Repo
For clarity and organization, each step (training, deployment, and client) is placed in different folders. However, it's essential to note that all training codes were executed in the same path without folder classifications. For the training script, utilize the downloaded data from the Lab 5.4 file link provided, as it contains all the necessary data.


