import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class CareerRecommender:

    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)

        # Convert comma-separated skills into text for TF-IDF
        self.df["Skills_Text"] = self.df["Skills"].apply(
            lambda x: " ".join(
                [skill.strip() for skill in x.split(",")]
            )
        )

        self.vectorizer = TfidfVectorizer()

        self.skill_matrix = self.vectorizer.fit_transform(
            self.df["Skills_Text"]
        )

    def recommend(self, user_skills, min_score=0.0):

        user_text = " ".join(user_skills)

        user_vector = self.vectorizer.transform([user_text])

        similarity_scores = cosine_similarity(
            user_vector,
            self.skill_matrix
        ).flatten()

        self.df["Match Score"] = similarity_scores

        recommendations = (
            self.df[self.df["Match Score"] > min_score]
            .sort_values(
                by="Match Score",
                ascending=False
            )
            .copy()
        )

        if recommendations.empty:
            recommendations = (
                self.df
                .sort_values(by="Match Score", ascending=False)
                .head(1)
                .copy()
            )

        user_skill_set = {
            skill.lower()
            for skill in user_skills
        }

        matched_skills = []
        missing_skills = []

        for skills in recommendations["Skills"]:

            role_skills = [
                skill.strip()
                for skill in skills.split(",")
            ]

            matched = []
            missing = []

            for skill in role_skills:

                if skill.lower() in user_skill_set:
                    matched.append(skill)
                else:
                    missing.append(skill)

            matched_skills.append(matched)
            missing_skills.append(missing)

        recommendations["Match %"] = (
            recommendations["Match Score"] * 100
        ).round(2)

        recommendations["Matched Skills"] = matched_skills
        recommendations["Missing Skills"] = missing_skills

        recommendations = recommendations[
            recommendations["Matched Skills"].apply(len) > 0
        ]

        if recommendations.empty:
            recommendations = (
                self.df
                .sort_values(by="Match Score", ascending=False)
                .head(1)
                .copy()
            )
            recommendations["Match %"] = (
                recommendations["Match Score"] * 100
            ).round(2)
            recommendations["Matched Skills"] = [[] for _ in range(len(recommendations))]
            recommendations["Missing Skills"] = [
                [s.strip() for s in skills.split(",")]
                for skills in recommendations["Skills"]
            ]

        return recommendations[
            [
                "Role",
                "Match %",
                "Matched Skills",
                "Missing Skills"
            ]
        ].reset_index(drop=True)