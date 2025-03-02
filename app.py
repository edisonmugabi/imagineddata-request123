import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

# reading the file
data = pd.read_excel("C:\\Users\\RTV-LPT1-233\\Desktop\\glfwork.xlsx")
st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style',unsafe_allow_html=True)
image=Image.open("C:/Users/RTV-LPT1-233/Desktop/LGF.png")
col1,col2=st.columns([1,0.9])
with col1:
    st.image(image,width=200)
    html_title = """
        <style>
        .title-test {
         font-weight:bold;
         padding:5px;
         border-radius:6px}
        </style>
        <center><h1 class="title-test">LGF Interactive Dashboard</h1></center>"""
with col2:
        st.markdown(html_title, unsafe_allow_html=True)
col3,col4,col5=st.columns([.1,0.45,0.45])
with col3:
    box_date=str(datetime.datetime.now().strftime('%Y-%m-%d'))
    st.write(f"last updated on: \n {box_date}")
with col4:
    fig=px.bar(data,x="District of operation",y="Number of MoUs signed with Schools",labels={"Number of MoUs signed with Schools":"Number of MoUs signed with Schools{No}"},
                title="Number of MoUs signed with Schools in each District",hover_data=["Number of MoUs signed with Schools"],
                template="gridon",height=500)
    st.plotly_chart(fig,use_container_width=True)
_, view1, dwn1, view2, dwn2=st.columns([0.15,0.20,0.20,0.20,0.20])   
with view1:
    expander=st.expander("district wise school MoUs")
    data1=data[["District of operation","Number of MoUs signed with Schools"]].groupby("District of operation").sum()
    expander.write(data1)
with dwn1:
    st.download_button("GetData", data1.to_csv().encode("utf-8"), file_name="school_MoUs.csv", mime="text/csv")

data["month_year"]=data['activity implementation date'].dt.strftime("%m'%Y")
result=data.groupby("month_year")["Number of MoUs signed with Schools"].sum().reset_index()

with col5:
    fig1=px.line(result,x="month_year",y="Number of MoUs signed with Schools",title="Mous signed over time",
                 template="gridon")
    st.plotly_chart(fig1,use_container_width=True)

with view2:
    expander1=st.expander("Month wise school MoUs")
    data2=result
    expander1.write(data2)
with dwn2:
    st.download_button("GetData", data2.to_csv().encode("utf-8"), file_name="school_MoUs_monthwise.csv", mime="text/csv")
st.divider()
result2 = data.groupby(["District of operation"])[["Number of teachers who participated in a training package on CBC interpretation and delivery",
                                                   "Number of master trainers who participated in a one-day ToT on the ACT Now App"]].sum().reset_index()
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=result2["District of operation"], y=result2["Number of teachers who participated in a training package on CBC interpretation and delivery"],
                      name="Number of teachers who participated in a training package on CBC interpretation and delivery"))
fig2.add_trace(go.Scatter(x=result2["District of operation"], y=result2["Number of master trainers who participated in a one-day ToT on the ACT Now App"], mode="lines",
                          name="Number of master trainers who participated in a one-day ToT on the ACT Now App", yaxis="y2"))
fig2.update_layout(
    title="""Number of teachers who participated in a training package on CBC interpretation 
    and delivery and Number of master trainers who participated in a one-day ToT on the ACT Now App""",
    xaxis=dict(title="District of operation"),
    yaxis=dict(title="No_teachers_trained_onCBC interpretation and delivery",showgrid=False),
    yaxis2=dict(title="No_master_trainers attendedToT on the ACT Now App", overlaying="y", side="right"),
    template="gridon",
    legend=dict(x=1, y=1)
)
_, col6 = st.columns([0.1, 1])
with col6:
    st.plotly_chart(fig2, use_container_width=True)
_, view3, dwn3 = st.columns([0.5, 0.45, 0.45])
with view3:
    expander2 = st.expander("District wise training details")
    expander2.write(result2)
with dwn3:
    st.download_button("GetData", result2.to_csv().encode("utf-8"), file_name="training_details.csv", mime="text/csv")
st.divider()