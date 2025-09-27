```python
import streamlit as st
import pandas as pd
import random
import re

# --- Page Configuration ---
st.set_page_config(
    page_title="Adaptive Scheduler",
    page_icon="⏰",
    layout="wide"
)

# --- Background Styling ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f4c75, #3282b8, #56cfe1);
    background-attachment: fixed;
}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("Adaptive Scheduler ⏰")

# --- Input Section ---
st.sidebar.header("Configuration")
tasks_input = st.sidebar.text_area("Enter tasks (comma separated):", "Task1, Task2, Task3")
members_input = st.sidebar.text_area("Enter team members (comma separated):", "Alice, Bob, Charlie")

# --- Processing Inputs ---
tasks = [t.strip() for t in tasks_input.split(",") if t.strip()]
members = [m.strip() for m in members_input.split(",") if m.strip()]

# --- Random Assignment ---
if st.sidebar.button("Generate Schedule"):
    if tasks and members:
        schedule = []
        for task in tasks:
            assigned = random.choice(members)
            schedule.append({"Task": task, "Assigned To": assigned})
        
        df = pd.DataFrame(schedule)
        st.subheader("Generated Schedule")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("Please provide both tasks and members.")
```
