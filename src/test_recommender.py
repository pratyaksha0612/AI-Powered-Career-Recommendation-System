from recommender import CareerRecommender

recommender = CareerRecommender("../data/jobs.csv")

skills = "Python SQL Machine Learning"

results = recommender.recommend(skills)

print("\nTop Career Recommendations:\n")
print(results)