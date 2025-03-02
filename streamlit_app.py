import streamlit as st
import time as t
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from PIL import Image

# Displaying an image
image = Image.open("C:/Users/RTV-LPT1-233/Desktop/LGF.png")
st.image(image, width=200)

# Title and headers
st.title("Luigi Gussani Foundation")
st.header("SEMS project 2025-2027")
st.subheader("The project aims to empower out of school school girls and boys plus teachers in 10 districts of sub Busoga region.")

# Information messages
st.info("Please fill in the details below to get started")
st.warning("Please fill all areas")
st.error("Please fill all areas")

# Data entry form
st.markdown("# Luigi Gussani Foundation Data entry Form")

with st.form("my_form"):
    # Writing text
    name_employer = st.text_input("Employer name")
    
    # Widgets
    gender = st.radio("Pick your gender", ["Male", "Female"])
    region = st.selectbox("Pick your region", ["Busoga", "Kampala", "Jinja"])
    color = st.multiselect("Pick your favourite color", ["Blue", "Yellow", "Red"])
    rating_project = st.select_slider("Pick your project rating", ["bad", "good", "excellent", "outstanding"])
    age_beneficiary = st.slider("Pick your age", 1, 100)
    
    # Number input
    age = st.number_input("Enter your age", 18, 100)
    
    # Text input
    email = st.text_input("Enter your email address")
    
    # Date input
    DOB = st.date_input("Enter your date of birth")
    
    # Time input
    DOBtime = st.time_input("Enter your time of birth")
    
    # File uploader
    picture = st.file_uploader("Upload your file")
    picture_name = picture.name if picture else "No file uploaded"
    
    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        with st.spinner("Submitting data..."):
            try:
                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                credentials_dict = st.secrets["gcp_service_account"]
                credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
                gc = gspread.authorize(credentials)
                
                spreadsheet = gc.open("Rawdata")
                worksheet = spreadsheet.sheet1
                
                # Prepare row data with timestamp
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                row_data = [timestamp, name_employer, email, age, DOB, DOBtime, gender, region, color, rating_project, age_beneficiary, picture_name]
                
                # Append row to sheet
                worksheet.append_row(row_data)
                
                st.success("Data submitted successfully!")
                st.balloons()
            
            except Exception as e:
                st.error(f"Error: {e}")

# Sidebar
st.sidebar.title("Welcome to the project")
st.sidebar.text_input("Mail address")
st.sidebar.text_input("Phone number")
st.sidebar.text_input("Password", type="password")
st.sidebar.button("Submit")
st.sidebar.radio("Job title", ["Project officer", "Project assistant", "M&E officer"])

# Data visualization
st.title("Bar chart")
df = pd.DataFrame(
    np.random.randn(50, 2),
    columns=['x', 'y']
)
st.bar_chart(df)

st.title("Line chart")
st.line_chart(df)

st.title("Area chart")
st.area_chart(df)
