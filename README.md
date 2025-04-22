# Thyroid-Cancer-Reoccurence-Detection

The primary goal of this project is to leverage machine learning to predict the likelihood of thyroid cancer recurrence in survivors. Early identification of      
   recurrence risk allows for proactive follow-up care and improved patient outcomes.

##  Project Description

- **Objective**: Build an accurate and accessible machine learning model to predict the probability of recurrence of throid cancer.
- **Dataset**: [Thyroid Cancer Dataset](https://www.kaggle.com/datasets/khwaishsaxena/thyroid-cancer-dataset)
- **ML Models Used**:
  - Logistic Regression 
  - Decision Tree 
  - LightGBM
  - XGBoost
  - Random Forest
    
## Libraries Used
- `Scikit-learn`  
- `numpy`  
- `pandas`  
- `seaborn`  
- `matplotlib`  
- `pickle`
  
##  Machine Learning Workflow

1. **Data Preprocessing**
   - Handling missing values  
   - Label encoding for categorical variables  

2. **Exploratory Data Analysis (EDA)**
   - Analyzing distribution of features  
   - Visualizing class balance  
   - Correlation analysis and feature importance
     
3. **Model Building**
   - Training multiple classifiers (Random Forest, XGBoost, LightGBM)  
   - Splitting data into train/test sets  
     
4. **Model Evaluation**
   - Performance metrics:  
     - Accuracy
     
## Features Used

- `Age`  
- `Gender`  
- `Smoking`  
- `HxSmoking`  
- `HxRadiotherapy`  
- `Thyroid Function`  
- `Physical Examination`  
- `Adenopathy`  
- `Pathology`  
- `Focality`  
- `Risk`  
- `T` (Tumor Size)  
- `N` (Lymph Node Involvement)  
- `M` (Metastasis)  
- `Stage`  
- `Response` (to treatment)  
- `Recurred` (Target Variable) 

## Results

After training and evaluating multiple machine learning models, the **Random Forest Classifier** was selected as the final model based on its performance across various evaluation metrics.

Random Forest outperformed other models like **XGBoost**, **LightGBM**, and **Logistic Regression**, demonstrating high generalization capability and consistent performance across both training and testing data.

### Final Model: Random Forest Classifier

- **Accuracy**: 98%

[Kaggle Notebook](https://www.kaggle.com/code/khwaishsaxena/thyroid-cancer-reoccurence-detection)
     
