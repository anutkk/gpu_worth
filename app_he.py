import streamlit as st
from compute import get_instances_within_budget, read_instances_from_excel

# Set the path to the Excel file
excel_file_path = 'instances.xlsx'  # Replace with your file path

# Load instances from the Excel file
instances = read_instances_from_excel(excel_file_path)

# Set the title of the app
st.title('מחשבון מופעי GPU של EC2')

# Ask the user for their budget
budget = st.number_input('הזן את התקציב שלך', min_value=0.0)

# When the 'Calculate' button is pressed
if st.button('חשב'):
    selected_instances, total_gpus, gpu_report = get_instances_within_budget(budget, instances)

    # Display the results
    st.write(f"נבחרו {len(selected_instances)} מופעים עם סה\"כ {total_gpus} כרטיסי מסך.")
    st.write(f"כרטיסי המסך: {gpu_report}")
