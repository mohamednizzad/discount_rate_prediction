# Disable Python Warnings
import warnings
warnings.filterwarnings("ignore")

import pickle
model = pickle.load(open('model.pkl','rb'))

# -----------------------------------------------

# Tkinter / Flask / #Streamlit / Django ....

# Run the command below in cmd to install streamlit
# pip install streamlit

# Import Streamlit
import streamlit as st

# Inialize the Streamlit App
st.set_page_config("Discount Rate Predictor for ABC Pharmacy")

input = st.number_input("Invoice Amount:",key="input")
submit = st.button("Discount Rate")

discountRate = model.predict([[input]])

if discountRate > 5:
	discountRate = 5

if submit:
	st.subheader("The Predicted Discount Rate is:")
	st.write(discountRate)

# Run using the command streamlit run fileName.py