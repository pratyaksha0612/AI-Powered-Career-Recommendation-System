import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class CareerRecommender:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)

        self.vectorizer = TfidfVectorizer()
        self.skill_matrix = self.vectorizer.fit_transform(self.df["Skills"])

    def recommend(self, user_skills, top_n=3):
        user_vector = self.vectorizer.transform([user_skills])

        similarity_scores = cosine_similarity(
            user_vector,
            self.skill_matrix
        ).flatten()

        self.df["Match Score"] = similarity_scores

        recommendations = (
            self.df.sort_values(
                by="Match Score",
                ascending=False
            )
            .head(top_n)
            .copy()
        )

        user_skill_set = set(
            skill.strip().lower()
            for skill in user_skills.split()
        )

        missing_skills = []

        for skills in recommendations["Skills"]:
            role_skills = set(
                skill.strip().lower()
                for skill in skills.split()
            )

            missing = role_skills - user_skill_set
            missing_skills.append(", ".join(missing))

        recommendations["Match %"] = (
            recommendations["Match Score"] * 100
        ).round(2)

        recommendations["Missing Skills"] = missing_skills

        return recommendations[
            ["Role", "Match %", "Missing Skills"]
        ]