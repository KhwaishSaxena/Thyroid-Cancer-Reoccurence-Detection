import streamlit as st

st.title(" Detect Thyroid Cancer Reoccurrence ")
st.write("""
        ## Objective
         The primary goal of this project is to leverage machine learning to assist in the early detection of thyroid cancer recurrence, enabling timely medical interventions and improved patient monitoring. By analyzing features such as age, tumor characteristics, treatment history, and follow-up data, the model provides a probabilistic prediction of cancer relapse risk in thyroid cancer survivors.
         
        ##Dataset
        The model is trained on a structured dataset consisting of clinical and diagnostic information of thyroid cancer patients. Key features include:
        
        -Age: Age of the patient at diagnosis or treatment
        -Gender: Biological sex of the patient
        -Smoking: Whether the patient is a current smoker
        -HxSmoking: History of smoking, including past usage
        -HxRadiotherapy: History of any radiotherapy treatment
        -Thyroid Function: Status of thyroid function (normal/abnormal)
        -Physical Examination: Findings from initial physical examinations
        -Adenopathy: Presence of lymph node enlargement
        -Pathology: Type of thyroid cancer diagnosed via biopsy
        -Focality: Whether the tumor is unifocal or multifocal
        -Risk: Categorization of cancer severity (e.g., low, intermediate, high risk)
        -T (Tumor): Tumor classification by size and local spread
        -N (Nodes): Lymph node involvement
        -M (Metastasis): Presence of distant metastases
        -Stage: Combined staging based on TNM classification
        -Response: Patient's response to initial treatment
        -Recurred (Target Variable): Whether the cancer has recurred post-treatment
        
        The model is evaluated using classification performance metrics like accuracy, precision, Confusion Matrix, F1-score, and AUC-ROC,   ensuring its clinical reliability and robustness.

         ## Technologies Used
        - **Streamlit**: For building the web application.
        - **Python**: Core programming language.
        - **Scikit-learn**: For machine learning model development.
        - **Pandas & NumPy**: For data manipulation and preprocessing.
        - **Matplotlib & Seaborn**: For visualizations.
        
        *Built with using Streamlit and Machine Learning*
    
         """)
