import streamlit as st
from recommender import CareerRecommender

st.set_page_config(
    page_title="AI Career Recommendation System",
    layout="wide"
)

recommender = CareerRecommender("data/jobs.csv")

st.title("AI-Powered Career Recommendation System")

st.write(
    "Enter your skills and discover the most suitable career paths."
)

skills = st.text_area(
    "Enter skills (separated by spaces)",
    placeholder="Python SQL Machine Learning"
)

if st.button("Get Recommendations"):

    if skills.strip():

        results = recommender.recommend(skills)

        st.subheader("Top Career Matches")

        st.dataframe(results, use_container_width=True)

    else:
        st.warning("Please enter at least one skill.")