import streamlit as st
from compute import get_instances_within_budget, read_instances_from_excel

# Set the path to the Excel file
excel_file_path = "Amazon EC2 Instance Comparison.xlsx"  # Replace with your file path

# Load instances from the Excel file
instances = read_instances_from_excel(excel_file_path)

# Set the title of the app
st.title('How many GPUs am I worth?')
st.markdown("### How many GPUs could be rented instead of me")


# Ask the user for their budget
budget = st.number_input('Enter your monthly salary in Israeli shekels', min_value=1000, max_value=200000)
st.caption("Privacy: I don't keep this data, but Streamlit Cloud may. Be careful and trust no one.")


# When the 'Calculate' button is pressed
if st.button('Calculate'):
    selected_instances, total_gpus, gpu_report = get_instances_within_budget(budget, instances)

    # Display the results
    st.markdown(f"## You are worth {total_gpus} GPUs.")
    st.markdown(f"#### Instead of hiring you, your employer could have rented {len(selected_instances)} instances with the following GPUs: {gpu_report}.")
    st.balloons()

    
st.caption("Code by [Shmuel Londner](https://github.com/anutkk).")
