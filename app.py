import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Student Performance Analyzer",
    layout="wide"
)

# Sidebar
st.sidebar.title("📚 Menu")
menu = st.sidebar.radio(
    "Navigate",
    ["Home", "Student Dataset", "Performance Visualization", "Student Form", "About App"]
)

# HOME PAGE
if menu == "Home":
    st.title("🎓 Student Performance Analyzer")
    st.write(
        "This application helps analyze student academic performance "
        "using simple data visualization techniques."
    )
    st.info("Use the sidebar to explore different sections of the application.")

# DATASET PAGE
elif menu == "Student Dataset":
    st.title("📊 Student Dataset")

    data = {
        "Student Name": ["Arun", "Divya", "Kiran", "Meena", "Ravi"],
        "Maths": [78, 85, 90, 72, 88],
        "Science": [80, 88, 92, 75, 90],
        "English": [75, 82, 89, 70, 85]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

# VISUALIZATION PAGE
elif menu == "Performance Visualization":
    st.title("📈 Performance Visualization")

    data = {
        "Subject": ["Maths", "Science", "English"],
        "Average Marks": [83, 85, 80]
    }

    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.bar(df["Subject"], df["Average Marks"])
    ax.set_xlabel("Subjects")
    ax.set_ylabel("Average Marks")
    ax.set_title("Average Marks per Subject")

    st.pyplot(fig)

# USER FORM PAGE
elif menu == "Student Form":
    st.title("📝 Student Marks Entry")

    name = st.text_input("Student Name")
    maths = st.number_input("Maths Marks", min_value=0, max_value=100)
    science = st.number_input("Science Marks", min_value=0, max_value=100)
    english = st.number_input("English Marks", min_value=0, max_value=100)

    if st.button("Submit"):
        avg = (maths + science + english) / 3
        st.success(f"Student {name}'s average score is {avg:.2f}")

# ABOUT PAGE
elif menu == "About App":
    st.title("ℹ️ About This Application")
    st.write("""
    **Student Performance Analyzer** is a Streamlit-based web application
    designed to analyze and visualize student academic data.

    **Features:**
    - Easy sidebar navigation
    - Student dataset display
    - Performance visualizations
    - Student marks input form

    🎯 **Future Scope:** Grade prediction, ranking system, database integration
    """)

st.markdown("---")
st.caption("© 2025 Student Performance Analyzer")
