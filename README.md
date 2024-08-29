# 🚀 Credit Card Fraud Detection

This repository contains the implementation of a project focused on detecting credit card fraud using machine learning techniques, specifically Logistic Regression and Random Forest models. The project uses a dataset of anonymized credit card transactions, aiming to enhance fraud detection accuracy and minimize financial losses.

---

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Project Objectives](#project-objectives)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [Code Structure](#code-structure)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Results and Analysis](#results-and-analysis)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## 📝 Project Overview

This project applies machine learning models, particularly Logistic Regression and Random Forest, to detect fraudulent transactions in credit card data. By focusing on feature selection and hyperparameter tuning, the project enhances the models' performance, achieving high accuracy, precision, and recall.

---

## 🎯 Project Objectives

1. **Study Current Fraud Detection Methods**
2. **Develop and Test Machine Learning Models**
3. **Enhance Data Preparation and Feature Selection**
4. **Evaluate Model Performance**
5. **Improve Real-Time Fraud Detection**
6. **Minimize Financial Losses**
7. **Ensure Compliance with Security Regulations**
8. **Provide Recommendations for Financial Institutions**

---

## 💻 Installation Instructions

### Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.x** installed on your machine.
- Basic understanding of **Python**, **machine learning**, and **data science** concepts.

### Installing Dependencies

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/credit-card-fraud-detection.git
   cd credit-card-fraud-detection

Create and activate a virtual environment (optional but recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt

## 🚀 Usage Instructions

### Data Preprocessing

- The dataset is included in the repository as `creditcard.csv`.
- Use the `credit_card_fraud_detection.ipynb` script to clean and prepare the data.

### Model Training and Evaluation

- Train models using `logistic_regression.ipynb` and `random_forest.ipynb`.
- Evaluate the models on the test set to assess their performance.

### Visualization

- Generate visualizations such as ROC curves .

---

## 🗂️ Code Structure

- **`credit_card_fraud_detection.py`**: Handles data cleaning, feature selection, and dataset balancing.
- **`logistic_regression_model_code.py`**: Trains and evaluates the Logistic Regression model.
- **`random_forest_model_code.py`**: Trains and evaluates the Random Forest model.

---

## 📈 Model Training and Evaluation

### Logistic Regression

- **Training**:
  - Trains on selected features (`Time`, `V1`, `V2`, `Amount`).
  - Hyperparameter tuning via `GridSearchCV`.
- **Evaluation**:
  - Produces accuracy, precision, recall, F1 score, and ROC curves.

### Random Forest

- **Training**:
  - Uses `n_estimators=100` with feature selection and hyperparameter tuning.
- **Evaluation**:
  - Outputs metrics similar to Logistic Regression, with added emphasis on minimizing false positives.

---

## 🏆 Results and Analysis

- **Logistic Regression**:
  - Achieved good accuracy with `V2` but struggled with recall.
- **Random Forest**:
  - Outperformed Logistic Regression with optimized thresholds, reaching up to 90% accuracy.

---

## 🙏 Acknowledgments

- Special thanks to my supervisor, **Mykola Gordovskyy**, for guidance and support.
- Data provided by the **Machine Learning Group** at Université Libre de Bruxelles, available on [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud).

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
