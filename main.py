
import pandas as pd
import streamlit as st
import plotly.express as px

import requests

complaints_url = "https://github.com/rashedulkabir730/DOB_Violations_Complaint_WebApp/releases/download/dataset/newcsv.csv"
violations_url = "https://github.com/rashedulkabir730/DOB_Violations_Complaint_WebApp/releases/download/dataset/violations.csv"

# Download the file
response = requests.get(complaints_url)
file_path = "newcsv.csv"
with open(file_path, "wb") as file:
    file.write(response.content)

response = requests.get(violations_url)
vio_file = "violations.csv"
with open(vio_file, "wb") as file:
    file.write(response.content)



# Read the dataset
complaints = pd.read_csv(file_path)
violations = pd.read_csv(vio_file)


st.title('NYC Building Violations & Complaints Dashboard')

violations['full_add'] = violations['full_add'].astype(str)
complaints['full_add'] = complaints['full_add'].astype(str)


address_list = violations['full_add'].unique().tolist()
selected_address = st.sidebar.selectbox("Select Building Address:", [""] + address_list)

def open_vio(addy):
    
    grouped_sum = addy.groupby(['Violation Status', 'Device Type'])['Violation Number'].count().reset_index()
    fig = px.bar(grouped_sum, 
                x='Violation Status', 
                y='Violation Number', 
                color='Device Type', 
                title=f'Violations for {selected_address}', 
                labels={'Violation Status': 'Violation Status', 'Violation Number': 'Number of Violations', 'Device Type': 'Device Type'},
                barmode='stack')
    return fig


def comments(addy):
    comments = addy['cleaned_comments'].dropna().unique()
    if comments.size > 0:
        st.write("Violation Description:")
        for comment in comments:
            st.write(f"- {comment}")
    

def com_viz(addy):
    priority_descriptions = {
        'A': 'Hazardous, Imminent Risk.',
        'B': 'Serious, No Imminent Risk.',
        'C': 'Non-Hazardous Violations.',
        'D': 'Quality-of-Life Problems.'
    }
    
    addy['Priority Description'] = addy['PRIORITY'].map(priority_descriptions)
    
    grouped = addy.groupby(['Year', 'PRIORITY','Priority Description'])['Complaint Category'].count().reset_index()
    fig = px.bar(grouped,
                 x='Year',
                 y='Complaint Category',
                 color='PRIORITY',
                 title=f'Complaints for {selected_address}',
                 labels={'Year':'Year', 'Complaint Category':'Number of Complaints','PRIORITY': 'Priority'},
                 hover_name='Priority Description',
                 hover_data={'Priority Description': True, 'PRIORITY': True, 'Complaint Category': True}
                 )  

    
    return fig

def compl_comments(addy):
    com = addy['COMPLAINT CATEGORY DESCRIPTION'].dropna().unique()
    
    if com.size > 0:
        st.write("Complaint Description:") 
        for comment in com:
            st.write(f"- {comment}")

if selected_address:
    if selected_address in violations['full_add'].values:
        
        result_df = violations[violations['full_add'] == selected_address]
         
        col1, col2 = st.columns(2)
        # Display bar chart in the first column
        with col1:
            fig = open_vio(result_df)
            st.plotly_chart(fig)
        # Display comments in the second column
        with col2:
            comments(result_df)


        
        result_df_com = complaints[complaints['full_add'] == selected_address]
        col3, col4 = st.columns(2)
        # Display complaint charts and comments
        with col3:
            fig_com = com_viz(result_df_com)
            st.plotly_chart(fig_com)
        with col4:
            compl_comments(result_df_com)

    else:
        st.write("Address not available in the database.")
else:
    st.write("Welcome! Please type in an address or select an address from the dropdown.")
