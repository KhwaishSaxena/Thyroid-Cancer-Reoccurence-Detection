import streamlit as st

st.title(" Detect Thyroid Cancer Reoccurrence ")
st.write("""
        ## Objective
         The primary goal of this project is to leverage machine learning to assist in the early detection of thyroid cancer recurrence, enabling timely medical interventions and improved patient monitoring. By analyzing features such as age, tumor characteristics, treatment history, and follow-up data, the model provides a probabilistic prediction of cancer relapse risk in thyroid cancer survivors.
         
        ## Dataset
        The model is trained on a structured dataset consisting of clinical and diagnostic information of thyroid cancer patients. Key features include:
        
        -Age
        -Gender
        -Smoking
        -HxSmoking
        -HxRadiotherapy
        -Thyroid Function
        -Physical Examination
        -Adenopathy
        -Pathology
        -Focality
        -Risk
        -T (Tumor)
        -N (Nodes)
        -M (Metastasis)
        -Stage
        -Response
        
        The model is evaluated using classification performance metrics like accuracy, precision, Confusion Matrix, F1-score, and AUC-ROC,   ensuring its clinical reliability and robustness.

         ## Technologies Used
        - **Streamlit**: For building the web application.
        - **Python**: Core programming language.
        - **Scikit-learn**: For machine learning model development.
        - **Pandas & NumPy**: For data manipulation and preprocessing.
        - **Matplotlib & Seaborn**: For visualizations.
        
        *Built with using Streamlit and Machine Learning*
    
         """)
