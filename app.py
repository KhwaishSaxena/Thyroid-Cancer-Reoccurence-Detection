import streamlit as st

def main():
    pg = st.navigation([
        st.Page('about.py', title = "Home", icon = ':material/home:'),
        #st.Page('prediction.py', title = "Predict", icon = ':material/stethoscope:'),
    ])
    pg.run()
    
if __name__  == "__main__":
    main()
