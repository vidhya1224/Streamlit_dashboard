import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Student Performance Analyzer",
    layout="wide"
)

# -----------------------------
# Initialize dataset in session
# -----------------------------
if "students" not in st.session_state:
    st.session_state.students = pd.DataFrame({
        "Student Name": ["Arun", "Divya", "Kiran", "Meena", "Ravi"],
        "Maths": [78, 85, 90, 72, 88],
        "Science": [80, 88, 92, 75, 90],
        "English": [75, 82, 89, 70, 85]
    })

# Sidebar
st.sidebar.title("📚 Menu")
menu = st.sidebar.radio(
    "Navigate",
    ["Home", "Student Dataset", "Performance Visualization", "Student Form", "About App"]
)

# -----------------------------
# HOME PAGE
# -----------------------------
if menu == "Home":
    st.title("🎓 Student Performance Analyzer")

    st.write(
        "Welcome to the Student Performance Analyzer dashboard. "
        "This application helps in monitoring and analyzing students' academic performance."
    )

    df = st.session_state.students

    # Summary Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("👨‍🎓 Total Students", len(df))
    col2.metric("📘 Average Maths Score", f"{df['Maths'].mean():.1f}")
    col3.metric("📗 Average Science Score", f"{df['Science'].mean():.1f}")

    st.markdown("---")

    st.success("📌 Tip: Add new students using the *Student Form* section.")

    st.write("""
    **Why this app?**
    - Helps teachers track student performance
    - Allows quick data entry
    - Visualizes subject-wise performance
    """)

# -----------------------------
# DATASET PAGE
# -----------------------------
elif menu == "Student Dataset":
    st.title("📊 Student Dataset")
    st.dataframe(st.session_state.students)

# -----------------------------
# VISUALIZATION PAGE
# -----------------------------
elif menu == "Performance Visualization":
    st.title("📈 Performance Visualization")

    df = st.session_state.students

    avg_marks = {
        "Subject": ["Maths", "Science", "English"],
        "Average Marks": [
            df["Maths"].mean(),
            df["Science"].mean(),
            df["English"].mean()
        ]
    }

    avg_df = pd.DataFrame(avg_marks)

    fig, ax = plt.subplots()
    ax.bar(avg_df["Subject"], avg_df["Average Marks"])
    ax.set_xlabel("Subjects")
    ax.set_ylabel("Average Marks")
    ax.set_title("Average Marks per Subject")

    st.pyplot(fig)

# -----------------------------
# STUDENT FORM PAGE
# -----------------------------
elif menu == "Student Form":
    st.title("📝 Student Marks Entry")

    name = st.text_input("Student Name")
    maths = st.number_input("Maths Marks", min_value=0, max_value=100)
    science = st.number_input("Science Marks", min_value=0, max_value=100)
    english = st.number_input("English Marks", min_value=0, max_value=100)

    if st.button("Add to Dataset"):
        if name.strip() == "":
            st.error("Please enter student name")
        else:
            new_row = {
                "Student Name": name,
                "Maths": maths,
                "Science": science,
                "English": english
            }

            st.session_state.students = pd.concat(
                [st.session_state.students, pd.DataFrame([new_row])],
                ignore_index=True
            )

            st.success(f"{name}'s marks added successfully!")

# -----------------------------
# ABOUT PAGE
# -----------------------------
elif menu == "About App":
    st.title("ℹ️ About This Application")
    st.write("""
    **Student Performance Analyzer** is a Streamlit-based web application
    designed to analyze and visualize student academic data.

    **Features:**
    - Easy sidebar navigation
    - Dynamic student dataset
    - Performance visualizations
    - Student marks input form

    🎯 **Future Scope:** Grade prediction, ranking system, database integration
    """)

st.markdown("---")
st.caption("© 2025 Student Performance Analyzer")
