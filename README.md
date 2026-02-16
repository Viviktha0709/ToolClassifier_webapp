# 🏭 ToolClassifier – ML-Powered Manufacturing Quality System

A production-oriented Machine Learning web application that classifies manufacturing tools as **Reject** or **Rework**.

Developed during my internship at **BHEL, Hyderabad**, this project demonstrates end-to-end ML deployment (from model training to a live Flask web application.)

---

## 🚀 What This Project Does

- Automates tool quality classification
- Reduces manual inspection effort
- Provides real-time predictions through a web interface
- Bridges ML experimentation with real-world deployment

---

## 📌 Need Analysis

In large-scale manufacturing environments, machine tools undergo continuous wear and require inspection to determine whether they should be **reworked** or **rejected**. Traditionally, this process is manual, time-consuming, and dependent on human judgment, leading to delays and inconsistencies in decision-making.

To improve efficiency and standardize quality control, there was a need for a data-driven system that could:

- Reduce manual inspection time  
- Provide consistent and unbiased decisions  
- Scale across large volumes of tools  
- Integrate into existing manufacturing workflows  

This project addresses that need by leveraging Machine Learning to automate tool classification and streamline the quality inspection pipeline.

---

## 🚀 Technical Features

- **Supervised Learning Model (Random Forest)**
  Implemented a Random Forest classifier for binary classification (Reject vs Rework), trained on structured manufacturing inspection data.

- Model Training & Evaluation Pipeline
  Performed data preprocessing, feature selection, train-test split, and model evaluation to ensure reliable predictive performance.

- Model Serialization for Deployment
  Serialized the trained model using Pickle/Joblib for seamless integration into the production backend.

- Backend Model Integration (Flask API)
  Integrated the trained model into a Flask-based backend to serve real-time inference through HTTP requests.

- End-to-End Inference Pipeline
  Implemented a prediction pipeline that handles:
  - Input validation
  - Data preprocessing
  - Feature alignment
  - Model inference
  - Output formatting

- Production-Oriented Web Interface
  Developed an interactive frontend (HTML/CSS) connected to the Flask backend to enable real-time tool classification.

- Real-World Industrial Application
  Designed and implemented during internship at BHEL, Hyderabad, focusing on improving manufacturing quality control workflows.

- Modular Project Structure
  Organized into separate components for training, model storage, backend logic, and UI to maintain clean architecture and scalability.

---

### Architectural Components

#### 1️⃣ Model Training Layer
- Dataset preprocessing and feature selection  
- Train-test split and model training (Random Forest)  
- Performance evaluation  
- Model serialization using Joblib  

#### 2️⃣ Application Layer (Backend)
- Flask server handles HTTP requests  
- Loads serialized ML model at runtime  
- Validates and preprocesses incoming input data  
- Performs real-time inference  

#### 3️⃣ Presentation Layer (Frontend)
- HTML/CSS-based interface  
- Accepts structured tool inspection parameters  
- Displays classification result to user  

---

## 📊 Model Evaluation

The model was evaluated using class-wise precision, recall, and F1-score due to significant class imbalance in the dataset (Reject: 12 samples, Rework: 399 samples in test set).
From a business perspective, maximizing recall for the Reject class is critical to avoid passing defective tools into the production pipeline.

### Test Performance (Random Forest)
 
<img width="435" height="183" alt="image" src="https://github.com/user-attachments/assets/5f90a871-48f9-44f7-96fc-05742edd6867" />

The model correctly identified **10 out of 12 Reject cases**, while maintaining perfect precision (no false positives for Reject).

### Confusion Matrix
<img width="375" height="305" alt="image" src="https://github.com/user-attachments/assets/e449d4a2-52ff-4cd1-90e8-73b0b205a1a5" />

- True Reject predicted as Reject: 10  
- True Reject predicted as Rework: 2  
- True Rework predicted as Rework: 399  
- False Reject predictions: 0  

This indicates strong minority-class detection while avoiding incorrect rejection of valid tools.

> Note: Due to the highly imbalanced dataset, evaluation focused on class-wise recall and F1-score rather than relying solely on overall accuracy.

## Web Application UI

<img width="776" height="373" alt="image" src="https://github.com/user-attachments/assets/4ee28772-df7b-41bf-801c-b2c2b7dd2ea5" />
<img width="818" height="386" alt="image" src="https://github.com/user-attachments/assets/6a9c3446-7157-4f6f-8aff-67965dd15889" />


