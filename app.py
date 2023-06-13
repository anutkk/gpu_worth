import streamlit as st
from compute import get_instances_within_budget, read_instances_from_excel

# Set the path to the Excel file
excel_file_path = "Amazon EC2 Instance Comparison.xlsx"  # Replace with your file path

# Load instances from the Excel file
instances = read_instances_from_excel(excel_file_path)

# Set the title of the app
st.title('How many GPUs am I worth?')

# Ask the user for their budget
budget = st.number_input('Enter your salary in Israeli shekels', min_value=0.0)

# When the 'Calculate' button is pressed
if st.button('Calculate'):
    selected_instances, total_gpus, gpu_report = get_instances_within_budget(budget, instances)

    # Display the results
    st.write(f"Selected {len(selected_instances)} instances with total of {total_gpus} GPUs.")
    st.write(f"GPUs: {gpu_report}")
