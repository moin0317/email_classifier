import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import pickle

# Load dataset
df = pd.read_csv("combined_emails_with_natural_pii.csv")

# Features and target
X = df['email']
y = df['type']

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create a pipeline: TF-IDF Vectorizer + Random Forest Classifier
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=5000)),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train the model
pipeline.fit(X_train, y_train)

# Save the trained model to a file
with open("classifier_model/email_classifier.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Model trained and saved to 'classifier_model/email_classifier.pkl'")

