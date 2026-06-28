import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return None
    return pd.read_csv(file_path)

def recommend_roles(user_skills, df, top_n=3):
    # Combine the user skills into a single string for vectorization
    user_skills_str = " ".join(user_skills)
    
    # Extract the skills from the dataset
    job_skills = df['skills'].tolist()
    
    # 1. Ingestion: Include user's skills as the first item in the list
    all_skills = [user_skills_str] + job_skills
    
    # 2. Process & Scoring: Apply TF-IDF and calculate Cosine Similarity
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_skills)
    
    # Calculate cosine similarity between the user profile (index 0) and all job roles
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    # 3. Sorting: Add scores to the dataframe and sort in descending order
    df['similarity_score'] = cosine_sim
    df_sorted = df.sort_values(by='similarity_score', ascending=False)
    
    # 4. Filtering: Get the Top-N roles to prevent choice overload
    top_roles = df_sorted.head(top_n)
    return top_roles

def main():
    print("==================================================")
    print("      Tech Stack Recommender (Project 3)          ")
    print("==================================================\n")
    
    # Load dataset
    csv_path = 'raw_skills.csv'
    df = load_data(csv_path)
    if df is None:
        return
        
    print("Please enter at least 3 skills you are interested in or possess.")
    print("Example: Python, Cloud Computing, Automation")
    user_input = input("\nEnter your skills (comma-separated): ")
    
    # Clean and split the user input
    user_skills = [skill.strip() for skill in user_input.split(',')]
    
    if len(user_skills) < 3 and len(user_skills[0]) > 0:
        print("\nWarning: For best results, it's recommended to provide at least 3 skills.")
    
    if not user_input.strip():
        print("No skills provided. Exiting.")
        return
        
    print("\nCalculating recommendations based on TF-IDF and Cosine Similarity...\n")
    
    # Get recommendations
    recommendations = recommend_roles(user_skills, df, top_n=3)
    
    print("--- TOP 3 RECOMMENDED ROLES ---")
    for index, row in recommendations.iterrows():
        role = row['role']
        score = row['similarity_score']
        matched_skills = row['skills']
        # Convert score to an intuitive percentage
        match_percentage = round(score * 100, 2)
        print(f"\n{role} - {match_percentage}% Match")
        print(f"Required Skills: {matched_skills}")

if __name__ == "__main__":
    main()
