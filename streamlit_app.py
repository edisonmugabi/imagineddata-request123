import streamlit as st
import time as t
import pandas as pd
import numpy as np

# Displaying an image
st.image("LGF.png", width=200)

# Title and headers
st.title("Luigi Gussani Foundation")
st.header("SEMS project 2025-2027")
st.subheader("The project aims to empower out of school school girls and boys plus teachers in 10 districts of sub Busoga region.")

# Information messages
st.info("Please fill in the details below to get started")
st.warning("Please fill all areas")
st.error("Please fill all areas")
st.success("Thank you, you have updated all areas")

# Writing text
st.write("employer name")

# Data entry form
st.markdown("# Luigi Gussani Foundation Data entry Form")
st.markdown(":moon:")
st.text("outcome section")
st.latex(r''' a+b x^2  + c = 0''')
st.caption("This is a caption")

# Widgets
st.checkbox("login")
st.button("click")
st.radio("pick your", ["Male", "Female"])
st.selectbox("pick your region", ["Busoga", "Kampala", "Jinja"])
st.multiselect("pick your favourite color", ["Blue", "Yellow", "Red"])
st.select_slider("pick your project rating", ["bad", "good", "excellent", "outstanding"])
st.slider("pick your age", 1, 100)

# Number input
st.number_input("Enter your age", 18, 100)

# Text input
st.text_input("Enter your email address")

# Date input
st.date_input("Enter your date of birth")

# Time input
st.time_input("Enter your time of birth")

# Text area
st.text_area("welcome to the project.hello mjosh")

# File uploader
st.file_uploader("Upload your file")

# Color picker
st.color_picker("pick your favourite color")

# Displaying progress
st.progress(50)

# Displaying spinner
with st.spinner("waiting"):
    t.sleep(5)
    st.success("completed")

# Displaying balloons
st.balloons()

# Sidebar
st.sidebar.title("welcome to the project")
st.sidebar.text_input("mail address")
st.sidebar.text_input("phone number")
st.sidebar.text_input("password")
st.sidebar.button("submit")
st.sidebar.radio("job title", ["project officer", "project assistant", "M&E officer"])

# Data visualization
st.title("bar chart")
df = pd.DataFrame(
    np.random.randn(50, 2),
    columns=['x', 'y']
)
st.bar_chart(df)

st.title("line chart")
st.line_chart(df)

st.title("area chart")
st.area_chart(df)